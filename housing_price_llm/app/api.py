from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
from catboost import Pool
import pandas as pd
import os

app = FastAPI()

# Allow all origins (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model
MODEL_PATH = "../models/catboost_price_model.pkl"
model = joblib.load(MODEL_PATH)

CAT_FEATURE_INDEXES = [0, 5, 9]

@app.post("/predict")
def predict_price(payload: dict):
    df = pd.DataFrame([payload])

    df = df[[
        "MSZoning", "LotArea", "OverallQual", "OverallCond",
        "YearBuilt", "HouseStyle", "BedroomAbvGr", "FullBath",
        "GrLivArea", "Neighborhood", "GarageCars"
    ]]

    pool = Pool(df, cat_features=CAT_FEATURE_INDEXES)
    prediction = model.predict(pool)[0]

    return {"predicted_price": float(prediction)}
