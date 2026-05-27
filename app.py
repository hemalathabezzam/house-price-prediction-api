from fastapi import FastAPI
import pandas as pd
import joblib
from main import HouseData

app= FastAPI()

# load model
model= joblib.load('house_price_model.pkl')

@app.get('/')
def home():
    return {'message':'House Price Prediction API Running'}

@app.get('/Welcome')
def get_name(name:str):
    return {'Welcome':f'{name}'}

@app.post('/predict')
def predict(data:HouseData):
    input_data = pd.DataFrame([[ 
    data.OverallQual,
    data.GrLivArea,
    data.GarageCars,
    data.TotalBsmtSF,
    data.FullBath
]], columns=[
    "OverallQual",
    "GrLivArea",
    "GarageCars",
    "TotalBsmtSF",
    "FullBath"
])
    prediction= model.predict(input_data)
    return {'Predicted House Price': float(prediction[0])}
