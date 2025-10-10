from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import sqlite3
import bcrypt
from datetime import datetime
import pandas as pd
import joblib
from rapidfuzz import fuzz
from fastapi.middleware.cors import CORSMiddleware


# python -m uvicorn Backend.master_api:app --reload

app = FastAPI(title="Hospital Management System API")
db_path = "c:\\Users\\Dell\\Desktop\\X Pay DataBase\\X Hospital DataBase.db"  # Raw string for Windows path

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- SEARCH --------------------
@app.post("/search")
def search_hospitals(query: str = Form("")):
    query = query.strip().lower()
    if not query:
        return JSONResponse({"error": "Query is required."}, status_code=400)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT hospital_name, hospital_rating, address, mobile_number, city, state, illness_type
        FROM hospitals
    """)
    hospital_rows = cursor.fetchall()

    cursor.execute("""
        SELECT doctor_name, specialization, hospital_name
        FROM add_doctor
    """)
    doctor_rows = cursor.fetchall()

    conn.close()

    hospital_matches = []
    for row in hospital_rows:
        h_name, rating, address, mobile, city, state, illness = row
        score = max([
            fuzz.partial_ratio(query, h_name.lower()),
            fuzz.partial_ratio(query, illness.lower()),
            fuzz.partial_ratio(query, city.lower()),
            fuzz.partial_ratio(query, state.lower())
        ])
        if score > 50:
            hospital_matches.append((score, row))

    doctor_matches = []
    for d_name, spec, h_name in doctor_rows:
        score = max([
            fuzz.partial_ratio(query, d_name.lower()),
            fuzz.partial_ratio(query, spec.lower()),
            fuzz.partial_ratio(query, h_name.lower())
        ])
        if score > 50:
            doctor_matches.append((score, {
                "doctor_name": d_name,
                "specialization": spec,
                "hospital_name": h_name
            }))

    hospital_matches = sorted(hospital_matches, key=lambda x: (-x[0], -float(x[1][1])))[:5]
    doctor_matches = sorted(doctor_matches, key=lambda x: -x[0])[:5]

    results = {
        "hospitals": [
            {
                "hospital_name": r[0],
                "rating": r[1],
                "address": r[2],
                "mobile_number": r[3],
                "city": r[4],
                "state": r[5],
                "illness_type": r[6]
            }
            for _, r in hospital_matches
        ],
        "doctors": [r for _, r in doctor_matches]
    }

    if not results["hospitals"] and not results["doctors"]:
        return JSONResponse({"error": "No matching results found."}, status_code=404)

    return results

# -------------------- SIGNUP/LOGIN --------------------
@app.post("/signup/user")
def signup_user(name: str = Form(...), mobile_number: str = Form(...), email_id: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO users (name, mobile_number, email_id, password, time) VALUES (?, ?, ?, ?, ?)",
                   (name, mobile_number, email_id, hashed_password.decode('utf-8'), current_time))
    conn.commit()
    conn.close()
    return {"message": "✅ User Signup Successfully!"}

@app.post("/signup/doctor")
def signup_doctor(doctor_name: str = Form(...), hospital_name: str = Form(...), specialization: str = Form(...), mobile_number: str = Form(...), email: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO doctor_register (name, hospital_name, specialization, mobile_number, password, email, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (doctor_name, hospital_name, specialization, mobile_number, hashed_password.decode('utf-8'), email, current_time))
    conn.commit()
    conn.close()
    return {"message": "✅ Doctor Signup Successfully!"}

@app.post("/login/user")
def login_user(email_id: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email_id = ?", (email_id,))
    user = cursor.fetchone()
    conn.close()
    if not user:
        return {"error": "❌ User not found"}
    stored_hash = user[0].encode('utf-8')
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return {"message": "✅ Login Successful"}
    return {"error": "❌ Invalid Password"}

@app.post("/login/doctor")
def login_doctor(email: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM doctor_register WHERE email = ?", (email,))
    doctor = cursor.fetchone()
    conn.close()
    if not doctor:
        return {"error": "❌ Doctor not found"}
    stored_hash = doctor[0].encode('utf-8')
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return {"message": "✅ Login Successful"}
    return {"error": "❌ Invalid Password"}

# -------------------- RECOMMENDATION --------------------
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

# -------------------- GET DOCTOR --------------------
@app.post("/get_doctor")
def get_doctor(city: str = Form(...), illness: str = Form(...)):
    city = city.strip().title()
    illness = illness.strip().title()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT doctor_name, specialization, hospital_name, mobile_number, email, license_id, city
        FROM add_doctor
        WHERE UPPER(city) = UPPER(?) AND UPPER(specialization) = UPPER(?)
    """, (city, illness))
    doctor_rows = cursor.fetchall()

    conn.close()

    if not doctor_rows:
        return {"error": f"No matching doctors found in {city} for illness '{illness}'."}

    doctors = []
    for row in doctor_rows:
        d_name, spec, h_name, mobile, email, license_id, d_city = row
        doctors.append({
            "doctor_name": d_name,
            "specialization": spec,
            "hospital_name": h_name,
            "mobile_number": mobile,
            "email": email,
            "license_id": license_id,
            "city": d_city
        })

    return {"doctors": doctors}

# -------------------- ADD DOCTOR --------------------
@app.post("/add_doctor")
def add_doctor(doctor_name: str = Form(...), hospital: str = Form(...), specialization: str = Form(...), mobile: str = Form(...), email: str = Form(...)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Basic validation
    if not all([doctor_name.strip(), hospital.strip(), specialization.strip(), mobile.strip(), email.strip()]):
        return JSONResponse({"error": "All fields are required."}, status_code=422)

    try:
        cursor.execute("""
            INSERT INTO add_doctor (doctor_name, hospital_name, specialization, mobile_number, email, license_id, city, time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (doctor_name.strip(), hospital.strip(), specialization.strip(), mobile.strip(), email.strip(), f"LIC-{len(str(doctor_name))}", "Unknown", current_time))
        conn.commit()
        conn.close()
        return {"message": "Doctor added successfully!"}
    except sqlite3.IntegrityError as e:
        conn.close()
        return JSONResponse({"error": "Duplicate entry or invalid data. Check email or mobile."}, status_code=422)
    except sqlite3.OperationalError as e:
        conn.close()
        return JSONResponse({"error": f"Database error: {str(e)}. Check table schema."}, status_code=500)
    except Exception as e:
        conn.close()
        return JSONResponse({"error": f"Failed to add doctor: {str(e)}"}, status_code=500)