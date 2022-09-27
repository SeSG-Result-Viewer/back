import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"ta on"}

@app.get("/sign-up")
def cadastrar():
    return {"cadastrando"}

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