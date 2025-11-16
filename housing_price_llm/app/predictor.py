# predictor.py
import joblib
import pandas as pd
from catboost import Pool

# Load the trained model
model = joblib.load("../models/catboost_price_model.pkl")

# Specify categorical feature indices (based on your training order)
CAT_FEATURES = [0, 5, 9]   # Example: MSZoning, HouseStyle, Neighborhood


def predict_price(features: dict) -> float:
    """
    Predicts house price given a dictionary of features.
    
    Args:
        features (dict): {
            "MSZoning": "RL",
            "LotArea": 8000,
            "OverallQual": 6,
            ...
        }

    Returns:
        float: Predicted house price
    """

    # Convert dict → DataFrame
    df = pd.DataFrame([features])

    # Ensure correct column order
    df = df[[
        "MSZoning", "LotArea", "OverallQual", "OverallCond",
        "YearBuilt", "HouseStyle", "BedroomAbvGr", "FullBath",
        "GrLivArea", "Neighborhood", "GarageCars"
    ]]

    # Wrap with CatBoost Pool
    pool = Pool(df, cat_features=CAT_FEATURES)

    # Predict
    prediction = model.predict(pool)[0]

    return float(prediction)


# # Example usage (you can remove this during deployment)
# if __name__ == "__main__":
#     sample = {
#         "MSZoning": "RL",
#         "LotArea": 9000,
#         "OverallQual": 6,
#         "OverallCond": 5,
#         "YearBuilt": 2010,
#         "HouseStyle": "2Story",
#         "BedroomAbvGr": 3,
#         "FullBath": 2,
#         "GrLivArea": 1800,
#         "Neighborhood": "CollgCr",
#         "GarageCars": 2
#     }

#     print("Predicted Price:", predict_price(sample))
