from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import pandas as pd
import joblib

#  python -m uvicorn Backend.ml_model:app --reload


app = FastAPI(title="Hospital Recommendation API")

# -------------------------
# Load Cleaned Data and Model
# -------------------------
df = pd.read_csv("Backend/clean_dataset.csv")
df.columns = df.columns.str.strip().str.lower()
df = df.dropna().drop_duplicates().astype(str)

model = joblib.load("Frontend/hospital_rf_model.joblib")
le_state = joblib.load("Frontend/le_state.joblib")
le_city = joblib.load("Frontend/le_city.joblib")
le_illness = joblib.load("Frontend/le_illness.joblib")
le_hospital = joblib.load("Frontend/le_hospital.joblib")

def safe_transform(le, value):
    return le.transform([value])[0] if value in le.classes_ else None

# -------------------------
# Recommendation Endpoint
# -------------------------
@app.post("/recommend")
def recommend(state: str = Form(...), illness: str = Form(...), city: str = Form(None)):
    state = state.strip().title()
    illness = illness.strip().title()
    city = city.strip().title() if city else None

    state_enc = safe_transform(le_state, state)
    illness_enc = safe_transform(le_illness, illness)
    city_enc = safe_transform(le_city, city) if city else -1

    if state_enc is None or illness_enc is None:
        return JSONResponse({"error": "Unknown State or Illness. Please check spelling."}, status_code=400)

    if city_enc == -1:
        candidates = df[(df['state'] == state) & (df['illness_type'] == illness)]
        if candidates.empty:
            return JSONResponse({"error": f"No hospital found for {state} - {illness}"}, status_code=404)
        best = candidates.sort_values(by='rating', ascending=False).iloc[0]
    else:
        try:
            pred_enc = model.predict([[state_enc, city_enc, illness_enc]])[0]
            pred_name = le_hospital.inverse_transform([pred_enc])[0]
            best = df[df['hospital_name'] == pred_name].iloc[0]
        except Exception as e:
            return JSONResponse({"error": f"Prediction failed: {str(e)}"}, status_code=500)

    return {
        "hospital_name": best['hospital_name'],
        "rating": best['rating'],
        "address": best['address'],
        "mobile_number": best['mobile_number'],
        "illness_type": best['illness_type'],
        "state": best['state'],
        "city": best['city']
    }
