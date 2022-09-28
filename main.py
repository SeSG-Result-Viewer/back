from http.client import HTTPException
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

@app.get("/login")
def login():
    return {"login"}

@app.get("/calc-metrics")
def calculateMetrics(arquivo, gs_size):
    dataFrame = pd.read_csv(arquivo)

    dataFrame['precision_gs'] = round(dataFrame['No. GS'] / dataFrame['No. Results'], 5)
    dataFrame['recall_gs'] = round(dataFrame['No. GS'] / gs_size, 5)
    dataFrame['recall_bsb'] = round(dataFrame['No. Total'] / gs_size, 5)
    dataFrame['gs_f_score'] = round(2 * (dataFrame['precision_gs'] * dataFrame['recall_gs']) / (dataFrame['precision_gs'] + dataFrame['recall_gs']), 5)
    
    dataFrame = dataFrame.fillna(0)

    return dataFrame.to_csv(arquivo + '-result-metrics.csv', index = False)