import streamlit as st
from predictor import predict_price

# Set page configuration
st.set_page_config(page_title="🏠 Housing Price Predictor", layout="wide")

# App title and description
st.title("🏡 Intelligent Housing Price Prediction System")
st.markdown("""
This app uses **Linear Regression** for predicting house prices  
and a **Large Language Model (LLM)** (from Hugging Face) to extract features from natural language input.  
Describe your house naturally, and get an intelligent, human-like price prediction.
""")

# User input section
st.markdown("### 🏘️ Describe the house")
user_input = st.text_area(
    "Example: 'A 3 bedroom 2 bath 2-story home built in 2010 in College Creek with a garage'",
    height=150
)

# When the user clicks Submit
if st.button("🔍 Submit"):
    if user_input.strip():
        with st.spinner("Analyzing description and predicting price..."):
            result = predict_price(user_input)

        # Create a clear and formatted output container
        with st.container():
            st.markdown(f"### 🏠 Estimated Price: ${result['predicted_price']:,.2f}")
            st.markdown("### 🔍 Extracted Features:")
            st.json(result['extracted_features'])

    else:
        st.warning("Please enter a house description before submitting.")

# Add a Clear button for convenience
if st.button("🧹 Clear"):
    st.experimental_rerun()
