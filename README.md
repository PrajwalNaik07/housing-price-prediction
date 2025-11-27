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
│ └── api.py # FastAPI backend
│
├── models/
│ └── catboost_price_model.pkl # Trained CatBoost model
│
├── data/
  └──train.csv # Dataset used for training
│
├── notebooks/
  └──EDA_and_Model_Training.ipynb # Notebook for training & EDA
├── frontend/
  └──index.html ## HTML/JS web client
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

## ▶️ How to Run the App (Client-Server Setup)

This application uses a separate FastAPI backend (api.py) to handle the model prediction and an HTML/JavaScript frontend (frontend/index.html) to collect user input.

### 1️⃣ Clone and Prepare

Follow the initial steps to clone the repository, create a virtual environment, and install dependencies.

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/housing-price-prediction.git
cd housing-price-prediction

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# 3. Install Dependencies (ensure uvicorn/fastapi are in requirements.txt)
pip install -r requirements.txt
```

### 2️⃣ Start the Prediction API (Backend)

The API is responsible for loading the CatBoost model and serving predictions on `http://localhost:8000.`

  1. Navigate to the directory containing the API script:
  ```bash
  cd app
  ```

  2. Run the FastAPI application using Uvicorn:
  ```bash
  uvicorn api:app --host 0.0.0.0 --port 8000 --reload
  ```
  _The --reload flag automatically restarts the server when code changes._

  You should see output indicating the server is running on http://127.0.0.1:8000. Keep this terminal window open and running.

### Run the Web Interface (Frontend)

The frontend is a simple HTML file that makes requests to the API running in the previous step.

Open a web browser (Chrome, Firefox, Edge, etc.).

Navigate to the location of your index.html file in the new frontend/ folder.

  -Direct File Path: Open your file explorer, navigate to housing-price-prediction/frontend/, and double-click index.html. The URL in your browser will look something like: file:///path/to/housing-price-prediction/frontend/index.html