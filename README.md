# 🏡 House Price Prediction App

A simple and interactive Streamlit application that predicts house prices using a trained **CatBoost Regressor** model on the Kaggle California Housing Price Dataset.

Users can input property details such as zoning, lot size, quality rating, living area, and neighborhood.  
The system returns an estimated house price along with the exact features used for prediction.

---

## 🚀 Features

- **CatBoost Regression Model** (excellent performance with categorical data)
- **Clean two-column Streamlit UI**
- **Descriptive dropdowns** mapped to model codes
- **Dynamic explanations** for zoning, neighborhoods, and architectural styles
- **Metadata-driven design** for easy updates
- Displays **prediction output + features summary**

---

## 📁 Project Structure


```
housing-price-predection/
├── app/
│ └── app.py # Streamlit frontend
│
├── models/
│ └── catboost_price_model.pkl # Trained CatBoost model
│
├── metadata.py # Mapping & dynamic explanations
│
├── train.csv # Dataset used for training
├── EDA_and_Model_Training.ipynb # Notebook for training & EDA
├── requirements.txt
└── README.md
```

## 🧠 Model Details

- **Model:** CatBoostRegressor  
- **RMSE:** ~25,000  
- **R² Score:** ~0.91  
- **Features Used:**  
  - MSZoning  
  - LotArea  
  - OverallQual  
  - OverallCond  
  - YearBuilt  
  - HouseStyle  
  - BedroomAbvGr  
  - FullBath  
  - GrLivArea  
  - Neighborhood  
  - GarageCars  

---

## ▶️ How to Run the App

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/housing-price-prediction.git
git checkout CatBoost
cd housing_price_llm/app
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```


### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run Streamlit App
```bash
cd app
streamlit run app.py
```

### 5️⃣ Open in Browser
```bash
http://localhost:8501
```
