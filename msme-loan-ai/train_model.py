import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.DataFrame({
    "cibil": [650, 720, 580, 800, 690],
    "monthly_turnover": [200000, 500000, 150000, 800000, 300000],
    "existing_emi": [20000, 10000, 30000, 5000, 15000],
    "net_profit": [40000, 150000, 20000, 300000, 70000],
    "default": [1, 0, 1, 0, 0]
})

X = data.drop("default", axis=1)
y = data["default"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "app/models/trained_model.pkl")