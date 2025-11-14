import streamlit as st
from predictor import predict_price

st.set_page_config(page_title="House Price Predictor", layout="wide")

st.title("🏡 Intelligent Housing Price Prediction System")
st.write("Provide the house details below to get a price prediction using a trained Linear Regression model.")

# ----------- Input Form Layout ---------------

st.header("🏘️ Enter House Details")

col1, col2, col3 = st.columns(3)

with col1:
    mszoning = st.selectbox("MSZoning", ["RL", "RM", "RH", "C", "FV"])
    overallqual = st.slider("Overall Quality (1–10)", 1, 10, 5)
    overallcond = st.slider("Overall Condition (1–10)", 1, 10, 5)
    garagecars = st.number_input("Garage Cars", 0, 4, 1)

with col2:
    lotarea = st.number_input("Lot Area (sq ft)", 1000, 50000, 7000)
    yearbuilt = st.number_input("Year Built", 1800, 2025, 2000)
    bedrooms = st.number_input("Bedrooms Above Ground", 1, 10, 3)
    fullbath = st.number_input("Full Bathrooms", 1, 4, 2)

with col3:
    grlivarea = st.number_input("Above Ground Living Area (sq ft)", 400, 6000, 1500)
    housestyle = st.selectbox("House Style", [
        "1Story", "1.5Fin", "1.5Unf",
        "2Story", "2.5Fin", "2.5Unf",
        "SLvl", "SFoyer"
    ])

    neighborhood = st.selectbox("Neighborhood", [
        "OldTown", "CollgCr", "Veenker", "Somerst", "Crawfor", "Gilbert",
        "NAmes", "Sawyer", "SawyerW", "Timber", "BrkSide", "NridgHt",
        "NoRidge", "Edwards"
    ])


# ----------- Predict Button ---------------

if st.button("Predict Price"):
    features = {
        "MSZoning": mszoning,
        "LotArea": lotarea,
        "OverallQual": overallqual,
        "OverallCond": overallcond,
        "YearBuilt": yearbuilt,
        "HouseStyle": housestyle,
        "BedroomAbvGr": bedrooms,
        "FullBath": fullbath,
        "GrLivArea": grlivarea,
        "Neighborhood": neighborhood,
        "GarageCars": garagecars
    }

    result = predict_price(features)

    st.success(f"🏠 Estimated House Price: **${result['predicted_price']:,.2f}**")

    with st.expander("🔍 Input Features Used"):
        st.json(result["features_used"])
