from fastapi import FastAPI,Form,HTTPException
import sqlite3
from datetime import datetime

now = datetime.now()

# here the main logic is that the user will enter the specializety what they need in 
# fronted and in and state so best doctor wil assign with there hospital vai doctor tabel



db_path = "c:\\Users\\Dell\\Desktop\\X Pay DataBase\\X Hospital DataBase.db"

app = FastAPI()

@app.get('/get doctor')
async def get_doctor_api() :
    print