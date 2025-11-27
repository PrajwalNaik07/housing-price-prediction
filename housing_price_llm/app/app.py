import streamlit as st
import joblib
from catboost import Pool
import pandas as pd

# ===============================
# Load CatBoost Model
# ===============================
@st.cache_resource
def load_model():
    return joblib.load("catboost_price_model.pkl")

model = load_model()

# ===============================
# Feature Mappings
# ===============================

MSZONING_MAP = {
    "Residential Low Density (RL)": "RL",
    "Residential Medium Density (RM)": "RM",
    "Residential High Density (RH)": "RH",
    "Commercial (C)": "C",
    "Floating Village (FV)": "FV"
}

HOUSESTYLE_MAP = {
    "One Story (1Story)": "1Story",
    "Two Story (2Story)": "2Story",
    "Split Level (SLvl)": "SLvl",
    "Split Foyer (SFoyer)": "SFoyer"
}

NEIGHBORHOOD_MAP = {
    "College Creek (CollgCr)": "CollgCr",
    "Crawford (Crawfor)": "Crawfor",
    "Old Town (OldTown)": "OldTown",
    "Northridge Heights (NridgHt)": "NrdgHt",
    "Northridge (NoRidge)": "NoRidge",
    "Veenker": "Veenker"
}

# CatBoost categorical column indexes (mapped after dataframe creation)
CAT_FEATURE_INDEXES = [0, 5, 9]  # MSZoning, HouseStyle, Neighborhood

# ===============================
# Sidebar – Full Feature Guide
# ===============================

st.sidebar.title("📘 Feature Guide (Hover for Tips)")
with st.sidebar.expander("Click to view detailed guide"):
    st.markdown("""
### 🏠 MSZoning  
Higher density zoning → lower price.

### 📏 LotArea  
Large plots → higher property value.

### ⭐ OverallQual  
Strongest driver of price besides square footage.

### 🛠 OverallCond  
Maintenance & quality of upkeep.

### 🏗 YearBuilt  
Newer homes usually worth more.

### 🏡 HouseStyle  
Modern styles (2Story) often priced higher.

### 🛏 BedroomAbvGr  
Only above-ground bedrooms count.

### 🛁 FullBath  
More bathrooms = higher value.

### 📐 GrLivArea  
Most important numeric feature.

### 📍 Neighborhood  
Massive impact on price due to location.

### 🚗 GarageCars  
1–3 cars have predictable value impact.
""")

# ===============================
# Main Title
# ===============================
st.title("🏠 California House Price Prediction (CatBoost Model)")
st.markdown("### 📋 Enter property details:")

# ===============================
# Input UI Layout
# ===============================

col1, col2 = st.columns(2)
user_inputs = {}

# ---------- Column 1 ----------
with col1:
    user_inputs["MSZoning"] = MSZONING_MAP[st.selectbox(
        "🏠 Zoning Classification",
        list(MSZONING_MAP.keys()),
        help="Defines how the land can be used. RL = most common residential zone."
    )]

    user_inputs["LotArea"] = st.number_input(
        "📏 Lot Size (sq ft)",
        min_value=500,
        max_value=50000,
        step=100,
        value=7500,
        help="Total area of the land parcel."
    )

    user_inputs["OverallQual"] = st.slider(
        "⭐ Overall Quality (1–10)",
        1, 10, 5,
        help="Quality of materials and finish. One of the strongest predictors."
    )

    user_inputs["OverallCond"] = st.slider(
        "🛠 Condition Rating (1–10)",
        1, 10, 5,
        help="Reflects the house's general maintenance and condition."
    )

    user_inputs["YearBuilt"] = st.number_input(
        "🏗 Year Built",
        min_value=1870,
        max_value=2030,
        value=2000,
        help="Newer homes typically have higher value."
    )

# ---------- Column 2 ----------
with col2:
    user_inputs["HouseStyle"] = HOUSESTYLE_MAP[st.selectbox(
        "🏡 House Style",
        list(HOUSESTYLE_MAP.keys()),
        help="Architectural style of the home."
    )]

    user_inputs["BedroomAbvGr"] = st.number_input(
        "🛏 Bedrooms (Above Ground)",
        min_value=1,
        max_value=10,
        value=3,
        help="Only above-ground bedrooms count."
    )

    user_inputs["FullBath"] = st.number_input(
        "🛁 Full Bathrooms",
        min_value=1,
        max_value=5,
        value=2,
        help="Total number of full bathrooms (shower/bath included)."
    )

    user_inputs["GrLivArea"] = st.number_input(
        "📐 Living Area (sq ft)",
        min_value=300,
        max_value=6000,
        value=1500,
        help="Above-ground finished square footage."
    )

    user_inputs["GarageCars"] = st.number_input(
        "🚗 Garage Capacity (Cars)",
        min_value=0,
        max_value=5,
        value=2,
        help="Number of cars that fit in the garage."
    )

st.markdown("---")

# ===============================
# Neighborhood Full Width
# ===============================
user_inputs["Neighborhood"] = NEIGHBORHOOD_MAP[st.selectbox(
    "🌍 Neighborhood",
    list(NEIGHBORHOOD_MAP.keys()),
    help="Neighborhood strongly affects pricing."
)]

st.markdown("---")

# ===============================
# Predict Button
# ===============================
if st.button("🔮 Predict House Price", use_container_width=True):

    df = pd.DataFrame([user_inputs])

    # Ensure correct column order
    df = df[[
        "MSZoning", "LotArea", "OverallQual", "OverallCond",
        "YearBuilt", "HouseStyle", "BedroomAbvGr", "FullBath",
        "GrLivArea", "Neighborhood", "GarageCars"
    ]]

    # CatBoost Pool for correct categorical processing
    pool = Pool(df, cat_features=CAT_FEATURE_INDEXES)

    prediction = model.predict(pool)[0]

    st.success(f"🏡 **Estimated House Price: ${prediction:,.2f}**")

    with st.expander("🔍 View All Input Features Used"):
        st.json(user_inputs)
