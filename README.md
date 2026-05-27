# House Price Prediction API

## Objective
Predict house prices using Machine Learning.

## Tech Stack
- FastAPI
- Scikit-learn
- Pandas
- Joblib

## Features Used
- OverallQual
- GrLivArea
- GarageCars
- TotalBsmtSF
- FullBath

## API Endpoint
POST /predict

## Run Locally

```bash
uvicorn app:app --reload
```

## Swagger UI
http://127.0.0.1:8000/docs