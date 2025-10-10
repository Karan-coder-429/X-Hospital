# ok lets serch doctor 

# python -m uvicorn Backend.search_bar:app --reload

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import sqlite3
from rapidfuzz import fuzz

app = FastAPI(title="Hospital Search API")

db_path = "c:\\Users\\Dell\\Desktop\\X Pay DataBase\\X Hospital DataBase.db"

@app.post("/search")
def search_hospitals(query: str = Form("")):
    query = query.strip().lower()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch hospital data
    cursor.execute("""
        SELECT hospital_name, hospital_rating, address, mobile_number, city, state, illness_type
        FROM hospitals
    """)
    hospital_rows = cursor.fetchall()

    # Optional: Fetch doctor data if needed
    cursor.execute("""
        SELECT name, specialization, hospital_name
        FROM doctors
    """)
    doctor_rows = cursor.fetchall()

    conn.close()

    # Match hospitals
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

    # Match doctors
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

    # Sort and limit
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
