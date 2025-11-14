import joblib
import pandas as pd

# Load model
model = joblib.load('../models/linear_regression.pkl')

def predict_price(features: dict):
    """Predict house price from structured input."""

    # Convert to DataFrame
    df = pd.DataFrame([features])

    # Add missing columns (required by the model)
    missing = set(model.feature_names_in_) - set(df.columns)
    for col in missing:
        df[col] = 0

    # Predict
    predicted = float(model.predict(df)[0])

    return {
        "predicted_price": predicted,
        "features_used": features
    }
