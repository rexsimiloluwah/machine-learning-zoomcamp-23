import os
import requests 

PREDICT_ENDPOINT = os.getenv("PREDICT_ENDPOINT", "http://localhost:9696/predict")

data = {"url": "http://bit.ly/mlbookcamp-pants"}

result = requests.post(PREDICT_ENDPOINT, json=data).json()
print(result)
