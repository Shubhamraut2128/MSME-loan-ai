import joblib
import numpy as np

MODEL_PATH = "app/models/trained_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def predict_risk(features: dict):
    model = load_model()

    input_array = np.array([[
        features["cibil"],
        features["monthly_turnover"],
        features["existing_emi"],
        features["net_profit"]
    ]])

    risk_score = model.predict_proba(input_array)[0][1] * 100
    return round(risk_score, 2)