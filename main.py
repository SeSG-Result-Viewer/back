from http.client import HTTPException

import pandas as pd
import json, re
import token_provider, security

from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from UserRepository import UserRepository
from schemas import SimpleUser, LoginData, User, calc_body

from database import get_db, create_db
from utils import get_logged_in_user

create_db()

app = FastAPI()

def starting(app):
    @app.on_event("startup")
    async def startup_event():
        create_db()
        db = get_db()
    
    @app.on_event("shutdown")
    def shutdown_event():
        print("dada")

starting(app)

#CORS
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get("/")
def home():
    return {"ta on"}

@app.post("/sign-up", status_code=status.HTTP_201_CREATED)
def sign_up_user(user: User, session: Session = Depends(get_db)):
    
    # Verifica se já existe um usuário com esse email
    registered_user = UserRepository(session).get_user_by_email(user.email)
    if registered_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail already registered!")

    # validação de formato de email
    if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user email format is invalid!") 

    # Hash para senha
    user.hashed_password = security.get_password_hash(user.hashed_password)

    # Cria usuário
    created_user = UserRepository(session).create(user)
    return {'name': created_user.name, 'email':created_user.email}

@app.post("/login")
def login(login_data: LoginData, session: Session = Depends(get_db)):
    password = login_data.password
    email = login_data.email

    user = UserRepository(session).get_user_by_email(email)
    # Se email não encontrado no BD
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid e-mail or password")

    valid_password = security.verify_password(password, user.hashed_password)
    # Se senha for inválida
    if not valid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid e-mail or password")

    #Gerar token JWT
    token: str = token_provider.create_access_token({'email': user.email})

    return {'name': user.name, 'email':user.email, 'access_token': token}

@app.get('/me', response_model=SimpleUser)        #para ver se o usuario esta logado
def me(user: User = Depends(get_logged_in_user)):
    return user

@app.post("/calc-metrics")
def calculate_metrics(resquest_body: calc_body):
    
    resquest_body.file = json.dumps(resquest_body.file)
    
    dataFrame = pd.read_json(resquest_body.file)
    dataFrame['precision_gs'] = round(dataFrame['No. GS'] / dataFrame['No. Results'], 5)
    dataFrame['recall_gs'] = round(dataFrame['No. GS'] / resquest_body.gs_size, 5)
    dataFrame['recall_bsb'] = round(dataFrame['No. Total'] / resquest_body.gs_size, 5)
    dataFrame['gs_f_score'] = round(2 * (dataFrame['precision_gs'] * dataFrame['recall_gs']) / (dataFrame['precision_gs'] + dataFrame['recall_gs']), 5)
    
    dataFrame = dataFrame.fillna(0)

    return dataFrame.to_json(orient='records')
