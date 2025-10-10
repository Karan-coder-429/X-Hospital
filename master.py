
# # here we have to test the data and whole code 


# from fastapi import FastAPI, Form
# import sqlite3
# import bcrypt
# from datetime import datetime
# now = datetime.now()


# # python -m uvicorn Backend.master_code:app --reload

# current_time = datetime.now# here strf concept or oter thing will onboard

# app = FastAPI(title="Auth API")
# db_path = "c:\\Users\\Dell\\Desktop\\X Pay DataBase\\X Hospital DataBase.db"

# @app.post("/signup/user")
# def signup(username: str = Form(...),mobile_number : str = Form(...),email_id : str = Form(...), password: str = Form(...)):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     password_1 = password.encode('utf-8')
#     salt = bcrypt.gensalt(rounds =12)
#     hashed_password = bcrypt.hashpw(password_1,salt)



#     cursor.execute("INSERT INTO users (name,mobile_number,email_id, password,time) VALUES (?,?,?, ?,?)", (username,mobile_number,email_id, hashed_password,current_time))
#     conn.commit()
#     conn.close()
#     return {"message": " User Signup successfully Done ✅"}

# @app.post("/signup/doctor")
# def signup(username: str = Form(...),hospital_name : str = Form(...),doctor_specilization : str = Form(...), mobile_number : str = Form(...),email_id : str = Form(...), password: str = Form(...)):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     password_1 = password.encode('utf-8')
#     salt = bcrypt.gensalt(rounds =12)
#     hashed_password = bcrypt.hashpw(password_1,salt)



#     cursor.execute("INSERT INTO doctor_register (username,hospital_name,doctor_specilization,mobile_number,email_id, password,time) VALUES (?,?,?, ?,?,?,?)", (username,mobile_number,email_id, hashed_password,current_time))
#     conn.commit()
#     conn.close()
#     return {"message": " Doctor Signup successfully Done ✅"}



# # in this logic where in frontend we have to select an role and after we will hit the api for differnt
# # 
# #  
# @app.post("/login/user ")
# def login(email_id: str = Form(...), password: str = Form(...)):
#     import bcrypt
#     import sqlite3

#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()

#     # Step 1: sirf stored hash lao
#     cursor.execute("SELECT password FROM users WHERE email_id = ?", (email_id,))
#     user = cursor.fetchone()

#     if user:
#         stored_hash = user[0]  # string form
#         # Step 2: compare plain password with stored hash
#         if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
#             return {"message": "Login successful"}
#         else:
#             return {"error": "Invalid credentials"}
#     else:
#         return {"error": "User not found"}
    




    
# @app.post("/login/doctor ")
# def login(email_id: str = Form(...), password: str = Form(...)):
#     import bcrypt
#     import sqlite3

#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()

#     # Step 1: sirf stored hash lao
#     cursor.execute("SELECT password FROM doctor_register WHERE email_id = ?", (email_id,))
#     user = cursor.fetchone()

#     if user:
#         stored_hash = user[0]  # string form
#         # Step 2: compare plain password with stored hash
#         if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
#             return {"message": "Login successful"}
#         else:
#             return {"error": "Invalid credentials"}
#     else:
#         return {"error": "User not found"}
    

from fastapi import FastAPI, Form
import sqlite3
import bcrypt
from datetime import datetime
from pydantic import BaseModel


# Run with:  python -m uvicorn Backend.master_code:app --reload

app = FastAPI(title="Auth API")

class UserSignup(BaseModel):
    name: str
    mobile_number: str
    email_id: str
    password: str

class DoctorSignup(BaseModel):
    doctor_name: str
    hospital_name: str
    specialization: str
    mobile_number: str
    email: str
    password: str

class LoginUser(BaseModel):
    email_id: str
    password: str

class LoginDoctor(BaseModel):
    email: str
    password: str


db_path = "c:\\Users\\Dell\Desktop\\X Pay DataBase\\X Hospital DataBase.db"
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # during local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# -------------------- USER SIGNUP --------------------
@app.post("/signup/user")
def signup_user(
    name: str = Form(...),
    mobile_number: str = Form(...),
    email_id: str = Form(...),
    password: str = Form(...)
):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO users (name, mobile_number, email_id, password, time)
        VALUES (?, ?, ?, ?, ?)
    """, (name, mobile_number, email_id, hashed_password.decode('utf-8'), current_time))

    conn.commit()
    conn.close()
    return {"message": "✅ User Signup Successfully!"}
# -------------------- DOCTOR SIGNUP --------------------
@app.post("/signup/doctor")
def signup_doctor(
    doctor_name: str = Form(...),
    hospital_name: str = Form(...),
    specialization: str = Form(...),
    mobile_number: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO doctor_register (name, hospital_name, specialization, mobile_number, password, email, time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (doctor_name, hospital_name, specialization, mobile_number, hashed_password.decode('utf-8'), email, current_time))

    conn.commit()
    conn.close()
    return {"message": "✅ Doctor Signup Successfully!"}


# -------------------- USER LOGIN --------------------

@app.post("/login/user")
def login_user(email_id: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE email_id = ?", (email_id,))
    user = cursor.fetchone()

    if not user:
        return {"error": "❌ User not found"}

    stored_hash = user[0].encode('utf-8')

    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return {"message": "✅ Login Successful"}
    else:
        return {"error": "❌ Invalid Password"}


# -------------------- DOCTOR LOGIN --------------------

@app.post("/login/doctor")
def login_doctor(email: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM doctor_register WHERE email = ?", (email,))
    doctor = cursor.fetchone()

    if not doctor:
        return {"error": "❌ Doctor not found"}

    stored_hash = doctor[0].encode('utf-8')

    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return {"message": "✅ Login Successful"}
    else:
        return {"error": "❌ Invalid Password"}



