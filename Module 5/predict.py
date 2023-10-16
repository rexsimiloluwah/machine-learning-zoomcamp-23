import pickle 

MODEL_PATH = "telco_churn_model_C=1.0.bin"

print("[INFO]: Loading the model")
with open(MODEL_PATH, "rb") as f_in:
    dv, model = pickle.load(f_in)

# Sample customer data
customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

print(f"[INFO]: Computing prediction")

def predict(customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    return y_pred 

y_pred = predict(customer)
print(f"Predicted churn probability: {y_pred}")