# Fraud Detection Model

A machine learning project to detect fraudulent transactions using logistic regression with advanced preprocessing techniques.

## 📊 Project Overview

This project implements a fraud detection system that can identify potentially fraudulent financial transactions. The model uses various transaction features to predict whether a transaction is legitimate or fraudulent.

### Key Features
- **Data Balancing**: Handles imbalanced dataset using upsampling techniques
- **Feature Engineering**: Comprehensive preprocessing pipeline
- **High Accuracy**: Achieves ~94.3% accuracy on test data
- **Production Ready**: Serialized model ready for deployment

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Installation
1. Clone the repository:
```bash
git clone <your-repository-url>
cd fraud-detection-model
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the model:
```python
python fraud_detection.py
```

## 📈 Model Performance

### Confusion Matrix Results
```
                Predicted
                Not Fraud    Fraud
Actual Not Fraud  1,202,788   68,062
       Fraud         76,640  1,194,273
```

### Performance Metrics
- **Accuracy**: 94.3%
- **Precision**: 94.6%
- **Recall**: 93.9%
- **F1-Score**: 94.2%

### Key Statistics
- **False Positive Rate**: 5.4% (68,062 legitimate transactions flagged)
- **False Negative Rate**: 6.0% (76,640 fraud cases missed)

## 🔧 Technical Implementation

### Data Preprocessing
1. **Feature Selection**: Removed irrelevant columns (`nameOrig`, `nameDest`, `isFlaggedFraud`, `step`)
2. **Data Balancing**: Used SMOTE upsampling to balance fraud vs non-fraud cases
3. **Feature Scaling**: Applied StandardScaler to numerical features
4. **Encoding**: One-hot encoding for categorical variables

### Model Architecture
```python
Pipeline([
    ('preprocessor', ColumnTransformer([
        ('onehotencoder', OneHotEncoder(drop='first'), ['type']),
        ('standardscaler', StandardScaler(), numerical_columns)
    ])),
    ('classifier', LogisticRegression(class_weight='balanced', max_iter=1000))
])
```

### Features Used
- **Categorical**: `type` (transaction type)
- **Numerical**: `amount`, `oldbalanceOrig`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`

## 📁 Project Structure
```
fraud-detection-model/
├── README.md
├── requirements.txt
├── fraud_detection.py          # Main model script
├── Model.pkl                   # Trained model file
├── data/
│   └── fraud_dataset.csv      # Dataset
├── images/
│   ├── confusion_matrix.png   # Performance visualizations
│   └── model_metrics.png
└── notebooks/
    └── exploration.ipynb      # Data exploration
```

## 🛠️ Usage

### Training the Model
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load and preprocess data
X = df_balanced.drop(['isFraud','nameOrig','nameDest','isFlaggedFraud','step'], axis=1)
y = df_balanced['isFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit pipeline
pipeline.fit(X_train, y_train)
```

### Making Predictions
```python
import pickle

# Load trained model
with open('Model.pkl', 'rb') as file:
    model = pickle.load(file)

# Make predictions
predictions = model.predict(X_new)
probabilities = model.predict_proba(X_new)
```

### Model Evaluation
```python
from sklearn.metrics import classification_report, confusion_matrix

# Evaluate model
y_pred = pipeline.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
```

## 📊 Data Description

The dataset contains financial transaction records with the following features:

| Feature | Description |
|---------|-------------|
| `type` | Type of transaction (PAYMENT, TRANSFER, CASH_OUT, DEBIT, CASH_IN) |
| `amount` | Transaction amount |
| `oldbalanceOrig` | Initial balance before transaction (origin) |
| `newbalanceOrig` | Final balance after transaction (origin) |
| `oldbalanceDest` | Initial balance before transaction (destination) |
| `newbalanceDest` | Final balance after transaction (destination) |
| `isFraud` | Target variable (1 if fraud, 0 if legitimate) |

## 🔍 Key Insights

1. **Transaction Types**: Certain transaction types (TRANSFER, CASH_OUT) are more prone to fraud
2. **Amount Patterns**: Large transactions often show different fraud patterns
3. **Balance Analysis**: Discrepancies in balance changes can indicate fraud
4. **Data Imbalance**: Original dataset heavily skewed toward legitimate transactions

## 🚀 Future Improvements

- [ ] Implement ensemble methods (Random Forest, XGBoost)
- [ ] Add more sophisticated feature engineering
- [ ] Implement real-time prediction API
- [ ] Add model interpretability with SHAP values
- [ ] Cross-validation for more robust evaluation
- [ ] Hyperparameter tuning with GridSearch

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Muhammad Haseeb Raza - hasiraza511@gmail.com
https://github.com/hasiraza/Fraud-Detection-Model.git
Project Link: [https://github.com/yourusername/fraud-detection-model](https://github.com/yourusername/fraud-detection-model)

## 🙏 Acknowledgments

- Dataset source: [Financial Transaction Dataset]
- Scikit-learn community for excellent ML tools
- Contributors and reviewers

---

**Note**: This model is for educational and research purposes. For production use in financial systems, additional validation, testing, and regulatory compliance measures are required.
