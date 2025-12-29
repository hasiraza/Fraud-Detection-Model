# 🚨 Fraud Detection System using Machine Learning

![Python](https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FE4B4B?logo=streamlit&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-1A73E8?logo=googlecloud&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview
The **Fraud Detection System** is an intelligent **Machine Learning–based application** designed to detect fraudulent transactions in real-time.  
It analyzes transaction patterns and identifies suspicious activities with high accuracy using trained ML models.

This system helps businesses **reduce financial losses**, **improve security**, and **automate fraud detection**.

---

## ⚙️ Features
✔ Real-time fraud prediction  
✔ Machine learning–based classification  
✔ Data preprocessing & feature engineering  
✔ API for model inference (FastAPI)  
✔ Interactive dashboard (Streamlit)  
✔ Model tracking with MLflow  
✔ Database storage (PostgreSQL)  
✔ Scalable & production ready  

---

## 🧠 Machine Learning Models
- Logistic Regression  
- Random Forest  
- XGBoost  
- Neural Networks  

Models are evaluated using:
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC-AUC  

---

## 🗂 Tech Stack
| Layer | Technology |
|------|-----------|
| Language | Python |
| ML | Scikit-Learn, TensorFlow, PyTorch |
| Data | Pandas, NumPy |
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | PostgreSQL |
| MLOps | MLflow |
| Version Control | Git, GitHub |

---

## 🚀 Installation & Setup

```bash
# Clone repository
git clone https://github.com/haseebraza511/fraud-detection-system.git

# Move into project
cd fraud-detection-system

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend API
uvicorn app.main:app --reload

# Run dashboard
streamlit run app.py
