# api.py
from fastapi import FastAPI
from predictor import predict_price

app = FastAPI()

@app.post("/predict")
def predict(features: dict):
    price = predict_price(features)
    return {"predicted_price": price}