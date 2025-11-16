import joblib
import pandas as pd

# Load your trained model
model = joblib.load('../models/catboost_price_model.pkl')

def predict_price(features: dict):
    """
    Takes a dictionary of structured inputs and predicts house price.

    Expected keys:
    MSZoning, LotArea, OverallQual, OverallCond, YearBuilt,
    HouseStyle, BedroomAbvGr, FullBath, GrLivArea,
    Neighborhood, GarageCars
    """

    # Convert input to DataFrame
    df = pd.DataFrame([features])

    # Ensure all columns expected by model exist
    missing_cols = set(model.feature_names_in_) - set(df.columns)
    for col in missing_cols:
        df[col] = 0

    # Predict price
    predicted = float(model.predict(df)[0])

    return {
        "predicted_price": predicted,
        "features_used": features
    }
