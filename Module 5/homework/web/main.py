import pickle 
from flask import Flask, request, jsonify

MODEL_PATH = "model2.bin"
DICT_VECTORIZER_PATH = "dv.bin"

print("[INFO]: Loading the vectorizer...")
with open(DICT_VECTORIZER_PATH, "rb") as f_in:
    dv = pickle.load(f_in)

print("[INFO]: Loading the model...")
with open(MODEL_PATH, "rb") as f_in:
    model = pickle.load(f_in)

app = Flask("bank_credit")

@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    credit = y_pred >= 0.5 

    result = {
        "credit_probability": float(y_pred), 
        "credit": bool(credit)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9697)

