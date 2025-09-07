# here we are going to write our new protype of new project x hospital
# this x hospital proejct for doctors and cusotmer all in one app

# ________________________________________________________________________________________________________
# Features of X Hospital Protype
# we Have Createdd Database for doctors and we have createa login and regirstoin system for doctors
# we have also created a doctor panel for doctors after login and registration
# we have also created a patient panel for patients after login and registration
# we have also To Create a appointment system for patients to book appointment with doctors
# and we have to create a system for doctors to check their appointments
# we have also to create a system for doctors to add patients and view patients
# we have also to create a system for doctors to update their profile and view their profile
# we have also to create a system for patients to view their profile and update their profile
# we have also to create a system for patients to view doctors and book appointment with doctors
# we have also to create a system for patients to view their appointments and cancel their appointments
# We have to create a login and registration system for patients
# We have to create a database for patients
# We have to create a database for appointments

# ______________________________________________________________________________________________________


import random
import sqlite3
import pwinput
import re
import bcrypt
import hashlib
from datetime import datetime
import os

current_time = datetime.now().strftime("%d-%b-%Y %I:%M:%p")
db_path = "c:\\Users\\Dell\\Desktop\\X Pay DataBase\\X Hospital DataBase.db"

def doctor_panel() :
 print("Ok Here is Your Doctor Section ✔")
 print("1. View Profile")
 print("2. Update Profile")
 print("3. Logout")
 print("4. Add Doctor")
 print("5.View Patients")
 print("6.Check Appointments")
 
 choice = input("Enter Your Choice : ")
#  if choice == "1" :
#   #view_profile()
#  elif choice == "2" :
#   update_profile()
#  elif choice == "3" :
#   logout()
#  else :
#   print("Invalid Choice ✔")

def doctor_login() :
 conn = sqlite3.connect(db_path)
 conn.row_factory = sqlite3.Row
 cursor = conn.cursor()
 print("Ok lets Do Login ✔")
 try :
   while True :
    name = input("Enter Your Name (Note The Name Should Be That Which You Were Use While Registration) : ").strip().title()
    for attempt in range(4) :
     password = pwinput.pwinput(prompt = "Enter Your X Hospital Password : ",mask = ".").strip().title()
     hash_password = hashlib.sha256(password.encode()).hexdigest()
     cursor.execute("SELECT * FROM doctors WHERE name = ? AND password = ?",(name,hash_password))
     rows = cursor.fetchall()
     for row in rows :
      user_name = (row["name"])
      
     if rows :
      print(f"\nWelcome - {user_name}!")
      doctor_panel()

      break
     else :
      attempt +=1
      print(f"Access Denied.You Have {3-attempt} Attempt Are left ✔")
     
    break

 except Exception as e :
  print("The Occured Error is ",e)

def doctor_registration() :
 conn = sqlite3.connect(db_path)
 conn.row_factory = sqlite3.Row
 cursor = conn.cursor()
 print("Ok lets Do Doctors Registaion ✔")
 try :
   while True :
    name = input("Enter Your Name (This name will use for login) : ").strip().title()
    m_number = input("Enter Your 10 Digit Mobile Number For Comunication & Message : +91 ").strip().title()
    
    pattern = r"^[6-9]\d{9}$"
    phone = int(m_number)
    if re.match(pattern,m_number) and len (m_number) == 10 :
     print("Ok Mobile Number Valided ✔")
     break
    else :
     print("Please Enter Valid Mobile Number ✔")
   while True :
        password = pwinput.pwinput(prompt = "Set Your X Hospital Password : ",mask = ".").strip().title()
        c_password = pwinput.pwinput(prompt = "Confirm Your X Hospital Password : ",mask = ".").strip().title()
        if password == c_password :
         hash_password = hashlib.sha256(password.encode()).hexdigest()
         print("Password Matched ✔")
         break
        else :
         print("Password Not Matched Please Try Again ✔")
   while True :
        email = input("Enter Your Email ID (This Email ID Will Use For Comunication & Message) : ").strip().lower()
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern,email) :
         print("Ok Email ID Valided ✔")
         break
        else :
         print("Please Enter Valid Email ID ✔")
   specialization = input("Enter Your Specialization (This Will Help To Find You Easily) : ").strip().title()
   while True :
        age = input("Enter Your Age : ").strip()
        if age.isdigit() and 25 <= int(age) <= 70 :
         age = int(age)
         print("Ok Age Valided ✔")
         break
        else :
          print("Please Enter Valid Age Between 25 to 70 ✔")
   while True :
     hospital_name = input("Enter Your Hospital Name Where You Are Working (This Will Help To Find You Easily) : ").strip().title()
     pattern = r"^[A-Za-z0-9][A-Za-z0-9\s\.\-]{2,99}$"
     if re.match(pattern,hospital_name) :
        print("Ok Hospital Name Valided ✔")
        break
     else :
        print("Please Enter Valid Hospital Name ✔")
   detail  = {
        "Name" : name,
        "Mobile Number" : phone,
        "Email ID" : email,
        "Specialization" : specialization,
        "Age" : age,
        "Hospital Name" : hospital_name,
        "password" : hash_password,
        "time" : current_time
    }
   cursor.execute("""INSERT INTO doctors (name,password,mobile_number,email,specialization,age,hospital_name,time)
                   VALUES (?,?,?,?,?,?,?,?)
                    """,
                    (detail["Name"],
                     detail["password"],
                     detail["Mobile Number"],
                     detail["Email ID"],
                     detail["Specialization"],
                     detail["Age"],
                     detail["Hospital Name"],
                     detail["time"]
                     ))
   conn.commit()
   print(f"{name}! You Are Successfully Registered With X Hospital ✔")
   print("Now You Can Login With Your Name & Password ✔")
  
    
 except Exception as e :
  print("The Occured Error is ",e)
  


def docotrs():
 print("OK here We Are in Doctors Panel ✔")
 while True :
  ask = input("\nAre You Already Joined With X Hospital \n1.)Yes \n2.)No \nYour Choice : ").strip()
  try :
   if ask == "1":
    doctor_login()

   elif ask == "2" :
    doctor_registration()

    break
   else :
    print("Please Select Valid Type So Algorithem Could Perform Task ✔")
  except Exception as e :
   print("The Occured Error is ",e)

def select_type() :
 while True :
  select = input("\nSelect Your Type \n1.)Doctors \n2.)Patients \nYour Choice : ").strip()
  if select == "1" :
   docotrs()
   break
  elif select == "2" :
   print
   break
  else :
   print("Please Select From Above Option ✔")


welcome = input("Welcome To X Hospital")

select_type()

