import joblib
import pandas as pd
import numpy as np
import json
from transformers import pipeline

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load('../models/linear_regression.pkl')

# List of all expected model columns
REQUIRED_COLUMNS = [
    'MSZoning', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt',
    'HouseStyle', 'BedroomAbvGr', 'FullBath', 'GrLivArea',
    'Neighborhood', 'GarageCars'
]

# -----------------------------
# Load Lightweight LLM
# -----------------------------
extractor = pipeline("text2text-generation", model="google/flan-t5-base")

# -----------------------------
# Feature Extraction with LLM
# -----------------------------
def extract_features_with_llm(text):
    prompt = f"""
You are an intelligent assistant that extracts housing features from natural language descriptions.
Carefully read the text and infer numeric and categorical features. Think step-by-step and ensure the JSON reflects the exact details mentioned.
If a detail is missing, use reasonable defaults.

---
Examples:

Example 1:
Input: "A 2-story house built in 2010 located in College Creek with 3 bedrooms, 2 full bathrooms, a 2-car garage, and about 1800 square feet of living space."
Output:
{{
  "MSZoning": "RL",
  "LotArea": 9000,
  "OverallQual": 6,
  "OverallCond": 6,
  "YearBuilt": 2010,
  "HouseStyle": "2Story",
  "BedroomAbvGr": 3,
  "FullBath": 2,
  "GrLivArea": 1800,
  "Neighborhood": "CollgCr",
  "GarageCars": 2
}}

Example 2:
Input: "A 1-story home built in 2005 in the Old Town neighborhood with 2 bedrooms, 1 bathroom, and a single-car garage."
Output:
{{
  "MSZoning": "RL",
  "LotArea": 8500,
  "OverallQual": 6,
  "OverallCond": 5,
  "YearBuilt": 2005,
  "HouseStyle": "1Story",
  "BedroomAbvGr": 2,
  "FullBath": 1,
  "GrLivArea": 1200,
  "Neighborhood": "OldTown",
  "GarageCars": 1
}}

Example 3:
Input: "An old 2-story home built in 1980 in Mitchell with 3 bedrooms, 2 full bathrooms, and a detached garage."
Output:
{{
  "MSZoning": "RL",
  "LotArea": 9500,
  "OverallQual": 5,
  "OverallCond": 6,
  "YearBuilt": 1980,
  "HouseStyle": "2Story",
  "BedroomAbvGr": 3,
  "FullBath": 2,
  "GrLivArea": 1600,
  "Neighborhood": "Mitchel",
  "GarageCars": 1
}}

---

Now extract features for:
"{text}"

Return ONLY valid JSON with the above fields.
    """

    response = extractor(prompt, max_new_tokens=400)
    raw_output = response[0]["generated_text"]

    try:
        json_start = raw_output.find("{")
        json_end = raw_output.rfind("}") + 1
        json_str = raw_output[json_start:json_end]
        features = json.loads(json_str)
    except Exception:
        features = {}

    return features



# -----------------------------
# Data Cleaning Helper
# -----------------------------
def clean_features(features: dict):
    """Sanitize and ensure compatibility with model pipeline."""
    cleaned = {}

    # Set safe defaults
    defaults = {
        'MSZoning': 'RL',
        'LotArea': 9000,
        'OverallQual': 6,
        'OverallCond': 5,
        'YearBuilt': 2005,
        'HouseStyle': '1Story',
        'BedroomAbvGr': 3,
        'FullBath': 2,
        'GrLivArea': 1500,
        'Neighborhood': 'CollgCr',
        'GarageCars': 2,
    }

    for col in REQUIRED_COLUMNS:
        val = features.get(col, defaults[col])

        # Handle missing or None
        if val in [None, "", "null", "NaN", np.nan]:
            val = defaults[col]

        # Convert types properly
        if col in ["MSZoning", "HouseStyle", "Neighborhood"]:
            val = str(val).strip()
        else:
            try:
                val = float(val)
            except Exception:
                val = defaults[col]

        cleaned[col] = val

    return cleaned


# -----------------------------
# Main Prediction Function
# -----------------------------
def predict_price(user_input):
    """Extract features from user text and predict price."""
    extracted = extract_features_with_llm(user_input)
    features = clean_features(extracted)

    # Ensure all model columns exist
    df = pd.DataFrame([features])
    for col in model.feature_names_in_:
        if col not in df.columns:
            df[col] = 0

    try:
        prediction = float(model.predict(df)[0])
    except Exception as e:
        print("Prediction error:", e)
        prediction = None

    return {
        "predicted_price": prediction,
        "extracted_features": features
    }
