import os
import streamlit as st
import pickle
import pandas as pd
import base64


# ------------------------------
# Background Functions
# ------------------------------
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .main > div {{
        padding-top: 2rem;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        margin: 1rem;
    }}

    .stSelectbox > div > div > div {{
        background-color: rgba(255, 255, 255, 0.9);
    }}

    .stButton > button {{
        background-color: rgba(255, 87, 51, 0.8);
        color: white;
        border: none;
        border-radius: 5px;
        backdrop-filter: blur(5px);
    }}

    .stButton > button:hover {{
        background-color: rgba(255, 87, 51, 1);
    }}

    .sidebar .sidebar-content {{
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(10px);
    }}

    h1, h2, h3 {{
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }}

    .stText {{
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


# ------------------------------
# Apply Background
# ------------------------------
bg_path = os.path.join("src", "background.jpg")
if os.path.exists(bg_path):
    set_background(bg_path)
else:
    st.warning("Background image not found! Make sure 'src/background.jpg' is in your repo.")


# ------------------------------
# Load Model
# ------------------------------
model_path = "Model.pkl"
if os.path.exists(model_path):
    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        model_loaded = True
    except Exception as e:
        st.error(f"Could not load model file: {e}")
        model_loaded = False
else:
    st.error("Model file not found! Upload 'Model.pkl' to your repo.")
    model_loaded = False


# ------------------------------
# App Layout
# ------------------------------
st.header("Fraud Detection System")
st.subheader("Enter Transaction Details")

# Payment method
payment_type = st.selectbox(
    "Select Payment Method",
    ["CASH_OUT", "TRANSFER", "PAYMENT", "CASH_IN", "DEBIT"]
)

# Input fields
amount = st.number_input("Enter Amount", min_value=0.0, value=1000.0)
old_balance_org = st.number_input("Old Balance Origin", min_value=0.0, value=0.0)
new_balance_orig = st.number_input("New Balance Origin", min_value=0.0, value=0.0)
old_balance_dest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)
new_balance_dest = st.number_input("New Balance Destination", min_value=0.0, value=0.0)


# ------------------------------
# Prediction
# ------------------------------
if st.button("Check for Fraud"):
    if model_loaded:
        try:
            input_data = pd.DataFrame({
                'type': [payment_type],
                'amount': [amount],
                'oldbalanceOrg': [old_balance_org],
                'newbalanceOrig': [new_balance_orig],
                'oldbalanceDest': [old_balance_dest],
                'newbalanceDest': [new_balance_dest]
            })

            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]

            if prediction == 1:
                st.error("🚨 FRAUD DETECTED!")
                st.write(f"Fraud Probability: {probability[1]:.2%}")
            else:
                st.success("✅ Transaction is Safe")
                st.write(f"Fraud Probability: {probability[1]:.2%}")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("Model not loaded. Cannot make prediction.")


# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.header("Fraud Detection Model")
st.sidebar.subheader("About")
st.sidebar.markdown(
    """
     This Fraud Detection Model is a Machine Learning model trained on raw transaction data.  
     It predicts the likelihood of a transaction being fraudulent.
    """
)

st.sidebar.subheader("How to use")
st.sidebar.markdown(
    """
    1. Enter transaction details.  
    2. Click **Check for Fraud**.  
    3. View the prediction result.  
    """
)

st.sidebar.subheader("Model Performance")
st.sidebar.markdown(
    """
    **Accuracy:** 94.31%  
    **Precision:** 94.61%  
    **Recall:** 93.97%  
    **Specificity:** 94.64%  
    **F1-Score:** 94.64%  
    """
)

st.sidebar.subheader("Contact Us")
st.sidebar.markdown(
    """
    📧 **Email:** hasiraza511@gmail.com  
    🔗 **LinkedIn:** [Profile](https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/)  
    💻 **GitHub:** [Repo](https://github.com/hasiraza)  
    """
)
