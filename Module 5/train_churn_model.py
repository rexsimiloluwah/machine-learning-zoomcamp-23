"""Training the Churn prediction model from Module 3"""
import os 
import pickle

import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split, KFold 
from sklearn.feature_extraction import DictVectorizer 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score 


DATASET_PATH = "../Module 3/dataset/telco_customer_churn.csv"
C = 1.0 
n_splits = 5

df = pd.read_csv(DATASET_PATH)

# Data preparation
df.columns = df.columns.str.lower().str.replace(" ", "_")

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(" ", "_")

df.totalcharges = pd.to_numeric(df.totalcharges, errors="coerce")
df.totalcharges = df.totalcharges.fillna(0)

df.churn = (df.churn == "yes").astype(int)

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

# Features to use
numerical = ['tenure', 'monthlycharges', 'totalcharges']

categorical = [
    'gender',
    'seniorcitizen',
    'partner',
    'dependents',
    'phoneservice',
    'multiplelines',
    'internetservice',
    'onlinesecurity',
    'onlinebackup',
    'deviceprotection',
    'techsupport',
    'streamingtv',
    'streamingmovies',
    'contract',
    'paperlessbilling',
    'paymentmethod',
]

def train(df_train, y_train, C=1.0):
    """Train the model"""
    dicts = df_train[categorical + numerical].to_dict(orient="records")

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)

    return dv, model 

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient="records")

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred 

# Perform KFold cross-validation
print("[INFO]: Performing KFold cross-validation")
kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []

for fold_idx, (train_idx, val_idx) in enumerate(kfold.split(df_full_train)):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.churn.values 
    y_val = df_val.churn.values 

    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    print(f"AUC score for fold {fold_idx}: {auc}")
    scores.append(auc)

print(f"C={C}, Mean AUC Score: {np.mean(scores):.3f} +- {np.std(scores):.3f}")

# Training the model
print("[INFO]: Training the model")
dv, model = train(df_full_train, df_full_train.churn.values, C=1.0)
y_test_pred = predict(df_test, dv, model)
y_test = df_test.churn.values

auc = roc_auc_score(y_test, y_test_pred)
print(f"AUC score for the full training dataset: {auc}")

# Save the model 
print("[INFO]: Saving the model")

if not os.path.isdir("models"):
    os.makedir("models")

output_file = f"models/telco_churn_model_C={C}.bin"

with open(output_file, "wb") as f_out:
    pickle.dump((dv, model), f_out)


