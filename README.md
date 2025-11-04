# 🏡 Intelligent Housing Price Prediction using Linear Regression and LLMs

This project integrates **Machine Learning (Linear Regression)** with **Large Language Models (LLMs)** to create an **intelligent, conversational house price prediction system**.
Instead of filling out rigid forms, users can describe a house in **natural language**, and the system automatically extracts the relevant features using an **LLM (Flan-T5)**, predicts the house price, and returns a **human-friendly response** through a **Streamlit interface**.

---

## 🧠 Overview

### 🎯 Objective

To develop an **interactive house price prediction system** that:

* Understands user queries in plain English.
* Extracts property features automatically using a pre-trained **LLM**.
* Predicts the price using a **trained Linear Regression model**.
* Displays results via an easy-to-use **Streamlit web app**.

### 🧩 Core Components

| Component                   | Description                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------- |
| **LLM (Flan-T5)**           | Extracts key property details (bedrooms, bathrooms, area, etc.) from natural text. |
| **Linear Regression Model** | Predicts the house price using extracted structured features.                      |
| **Streamlit Interface**     | Frontend for user interaction and real-time predictions.                           |
| **Training Notebook**       | Contains EDA, preprocessing, and model training.                                   |

---

## 🏗️ Project Structure

```
housing-price-predection/
├── app/
│   ├── app.py                     # Streamlit app entry point
│   ├── predictor.py               # Handles LLM + model prediction
│   └── llm_feature_extractor.py   # LLM-based feature extraction logic
├── models/
│   └── linear_regression.pkl      # Trained regression model
├── data/
│   └── train.csv                  # Training dataset
├── notebooks/
│   └── EDA_and_Model_Training.ipynb  # Model building and EDA
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/housing-price-prediction.git
cd housing-price-predection/app
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r ../requirements.txt
```

### 4️⃣ Download Model Files

Ensure `linear_regression.pkl` is inside `models/` and `train.csv` is available under `data/`.

---

## 🚀 Run the Streamlit App

```bash
streamlit run app.py
```

Once started, open the local URL shown in the terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## 💬 Example Input

> *A 2-story house built in 2010 located in College Creek with 3 bedrooms, 2 full bathrooms, a 2-car garage, and about 1800 square feet of living space.*

**Output:**
🏠 Estimated Price: **$201,105.22**
📋 Extracted Features:

```json
{
  "MSZoning": "RL",
  "LotArea": 9000,
  "OverallQual": 6,
  "OverallCond": 5,
  "YearBuilt": 2010,
  "HouseStyle": "2Story",
  "BedroomAbvGr": 3,
  "FullBath": 2,
  "GrLivArea": 1800,
  "Neighborhood": "CollgCr",
  "GarageCars": 2
}
```

---

## 📊 Model Performance

| Metric       | Value     |
| ------------ | --------- |
| **RMSE**     | 34,700.06 |
| **R² Score** | 0.843     |

---

## 🧩 Tech Stack

* **Python 3.11+**
* **scikit-learn** – Linear Regression model
* **Hugging Face Transformers** – Feature extraction using LLM
* **pandas, numpy** – Data preprocessing
* **Streamlit** – Web interface

---

## 🧠 Future Enhancements

* Integrate a fine-tuned LLM for better feature extraction accuracy.
* Include more advanced regression models (Random Forest, XGBoost).
* Deploy the app on AWS / Hugging Face Spaces for global access.

---

## 📚 References

1. [Kaggle House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
2. [Scikit-learn Documentation](https://scikit-learn.org/stable/)
3. [Hugging Face Transformers](https://huggingface.co/transformers/)
4. [Streamlit Documentation](https://docs.streamlit.io/)

