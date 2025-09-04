import streamlit as st
import pickle
import pandas as pd
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set background image
def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
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
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Apply background
try:
    set_background('src\\background.jpg')
except FileNotFoundError:
    st.warning("Background image 'background.jpg' not found.")

# Load model
try:
    with open('Model.pkl', 'rb') as file:
        model = pickle.load(file)
    model_loaded = True
except:
    st.error("Could not load model file")
    model_loaded = False

# Main header
st.header("Fraud Detection System")

# Input fields
st.subheader("Enter Transaction Details")

# Payment method
payment_type = st.selectbox("Select Payment Method", ["CASH_OUT", "TRANSFER", "PAYMENT", "CASH_IN", "DEBIT"])

# Transaction amount
amount = st.number_input("Enter Amount", min_value=0.0, value=1000.0)

# Old balance origin
old_balance_org = st.number_input("Old Balance Origin", min_value=0.0, value=0.0)

# New balance origin  
new_balance_orig = st.number_input("New Balance Origin", min_value=0.0, value=0.0)

# Old balance destination
old_balance_dest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)

# New balance destination
new_balance_dest = st.number_input("New Balance Destination", min_value=0.0, value=0.0)

# Predict button
if st.button("Check for Fraud"):
    if model_loaded:
        # Create input data
        input_data = pd.DataFrame({
            'type': [payment_type],
            'amount': [amount],
            'oldbalanceOrg': [old_balance_org],
            'newbalanceOrig': [new_balance_orig],
            'oldbalanceDest': [old_balance_dest],
            'newbalanceDest': [new_balance_dest]
        })
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        # Show result
        if prediction == 1:
            st.error("FRAUD DETECTED!")
            st.write(f"Fraud Probability: {probability[1]:.2%}")
        else:
            st.success("Transaction is Safe")
            st.write(f"Fraud Probability: {probability[1]:.2%}")
    else:
        st.error("Model not loaded. Cannot make prediction.")

# Sidebar
st.sidebar.header("Fraud Detection Model")
st.sidebar.subheader("About")
st.sidebar.markdown(
    """
     This Fraud Detection Model is Machine Learning Model train on Raw file data.
     This Model Predict according to given entered data.
    """
)

st.sidebar.subheader("How to use")
st.sidebar.markdown(
    """
    1. Enter Data In input boxes.
    2. Click on check
    3. You will show Prediction
    """
)

st.sidebar.subheader("Model Accuracy")
st.sidebar.markdown(
    """
    **Accuracy:** 94.31%
    
    **Precision:** 94.61%
    
    **Recall:** 93.97%
    
    **Specificity:** 94.64%
    
    **F1-Score:** 94.64%
    """
)

st.sidebar.subheader("Contact us")
st.sidebar.markdown(
    """
    **Email:** hasiraza511@gmail.com
    
    **Linkedin:** https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/
    
    **github:** https://github.com/hasiraza
    """
)
