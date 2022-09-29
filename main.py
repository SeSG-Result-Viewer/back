from http.client import HTTPException

import security
import token_provider
import utils
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"ta on"}

@app.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=User)
def sign_up_user(user: User, session: Session = Depends(get_db)):
    # Verifica se já existe um usuário com esse email
    registered_user = Repository(session).get_user_by_email(user.email)
    if registered_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail already registered!")

    # Criar usuário
    user.password = security.get_password_hash(user.password)    #hash para senha
    created_user = Repository(session).create(user)
    return created_user

@app.post("/login")
def login(login_data: LoginData, session: Session = Depends(get_db)):
    password = login_data.password
    email = login_data.email

    user = Repository(session).get_user_by_email(email)
    # Se email não encontrado no BD
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid e-mail or password")

    valid_password = security.verify_password(password, user.password)
    # Se senha for inválida
    if not valid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid e-mail or password")

    #Gerar token JWT
    token = token_provider.create_access_token({'sub': user.email})

    return {'user': user, 'access_token': token}
    #Se existir a classe "LoginSuccess"
    #return LoginSuccess(user=user, access_token=token)
    #e adiciona response_model=LoginSucesso

@app.get('/me', response_model=SimpleUser)        #para ver se o usuario esta logado
def me(user: User = Depends(get_logged_in_user)):
    return user


@app.get("/calc-metrics")
def calculateMetrics(arquivo, gs_size):
    dataFrame = pd.read_csv(arquivo)

    dataFrame['precision_gs'] = round(dataFrame['No. GS'] / dataFrame['No. Results'], 5)
    dataFrame['recall_gs'] = round(dataFrame['No. GS'] / gs_size, 5)
    dataFrame['recall_bsb'] = round(dataFrame['No. Total'] / gs_size, 5)
    dataFrame['gs_f_score'] = round(2 * (dataFrame['precision_gs'] * dataFrame['recall_gs']) / (dataFrame['precision_gs'] + dataFrame['recall_gs']), 5)
    
    dataFrame = dataFrame.fillna(0)

    return dataFrame.to_csv(arquivo + '-result-metrics.csv', index = False)
