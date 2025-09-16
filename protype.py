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

# ________________________________________________________________________________________________________

# - For Creating Offline Token Based System like JWT 

#we had an idea with that idaea our main problem login into every function will be removed for always
# when user will login into app like login into one fucntin we will create session.json andstore the datea
# user name ,password hash,session activat time, session ending time  ,token id uuid
# when user open any fucntion after login we will chreck user name ,token id,password,session time 
# and if it all okay we allow to use app and if its not good we will say to login 
# now our app is fucntion based for checking this session file while statring the fucntion
# we have to ask bhia how we could check user data 
# and when user session got end json automatic will delete

# __________________________________________________________________________________________________________


# we will create our algorithem that can find best nearrst hospital for peopel by entrr just there name 
# and we will use google map api for that and we will use geopy library for that


# _______________________________________________________________________________________________________

# we will introduce our otp system with your email section 
# user need to enter theri email id and we will access at that and we will verify that otp that generatee
# so lets go we will introduce this feature soon be ready guys

#v  _______________________________________________________________________________________________________________
# Testing Logic- 

# while Teting the whole app what we have to do this like as we know our main focus will on class what 
 #hosital assign by state and order of 3 rating we have to test all the aspect of it 
# and first check direct and check after ruining becasue there might be erorr

# we have done some blunder in while state to doctor data in telngana or other section 
# where i put wrong speliing of some city so we have to solve it



# i have to lots of things in x hospital i have done lots of thing that we have to our code has been crossed 4000 + line which is good for us now i have 

# created the state wise big hsopital data wiht lots of illness now the second thing is which have to create same logic for clinic system 

# and after that we ahve to add 100+ hospital with differnt city and state with each illness and we have many type of illenss kidney,neurology,heart,cancer,orhtodpadic
# eye etc.. + means we will have 7000+ row data for the hospital and that data we will use in our reocmedatin osystem and we wil create our recomesdation dssytem 

# very powerfull and verstile




# ______________________________________________________________________________________________________

# For Doctor Verfication we will use cnn 

# CNN for Doctor Verification
# Use case: Verify doctor credentials via document/image scans

# Input:

# Doctor license image

# Certificate scans

# Signature or ID card

# Model type:

# Convolutional Neural Network (CNN) for image classification

# Use pretrained models like ResNet or MobileNet for feature extraction

# Fine-tune on your dataset of verified vs fake documents

# Output:

# Binary classification: Verified ✅ / Suspicious ❌

# Confidence score for manual override


# ____________________________________________________________________________________________________-

#   For Model Training we will do like for big hospital we will make diffenrt dataset and use difernt
# suvpervised model for that 

import uuid
import random
import sqlite3
import pwinput
import re
import bcrypt
import hashlib
from datetime import datetime
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import lightgbm



unique_id = str(uuid.uuid4())


current_time = datetime.now().strftime("%d-%b-%Y %I:%M:%p")
db_path = "c:\\Users\\Dell\\Desktop\\X Pay DataBase\\X Hospital DataBase.db"

def doctor_view_profile() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  print("Ok Here we are at your profile section ✔")
  try :
    name = input("Enter Your Name : ").strip().title()
    password = pwinput.pwinput(prompt = "Enter Password To View Your Profile : ").strip().title()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM doctors WHERE name = ?AND password ?",(name,hash_password,))
    rows = cursor.fetchall()
    for row in rows :
     name_master = (row["name"])
     mobile_number = (row["mobile_number"])
     email = (row["email"])
     specilization = (row["specialization"])
     age = (row["age"])
     hospital_name = (row["hospital_name"])
    if rows :
      print(f"\nWelcome {name_master} \nMobile Number is : +91 {mobile_number} \nEmail id is : {email} \n{name_master} Specilization is : {specilization}\nThe AGE Of {name_master} is : {age} From : {hospital_name}")
    else :
      print("No Doctor Data Found ✔")
  except Exception as e :
    print ("The Occured Error is",e)

# ________________________________________________________________________________________________________
# This is file for update doctor file  


def name_update() :
  print("OK Lets Update Your Name ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    name = input("Enter Current Name : ").strip().title()
    cursor.execute("SELECT * FROM doctors WHERE name = ?",(name,))
    row =cursor.fetchone()
    if row :
     print("OK Your Name Got Confirmed ✔")
     new_name = input("Enter Your New Name : ").strip().title()
     cursor.execute("UPDATE doctos SET name = ? WHERE name = ?",(new_name,name))
     conn.commit()
     print(f"The Name Updated From : {name} To {new_name} ✔")
    else :
     print("NO Name Data Avalibal with This Name ✔")
  except Exception as e :
    print("The Occured Error is ",e)


def mobile_number_update() :
  print("Ok Lets Update Mobile Number Detail ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    M_number = input("Enter Current Mobile Number : +91 ").strip()
    cursor.execute("SELECT * FROM doctors WHERE mobile_number = ?",(M_number,))
    row =cursor.fetchone()
    if row :
     print("OK Your Mobile Number  Got Confirmed ✔")
     new_number  = input("Enter Your New Name : ").strip().title()
     cursor.execute("UPDATE doctos SET mobile_number = ? WHERE name = ?",(new_number,M_number))
     conn.commit()
     print(f"Ok The Mobile Number Change From : +91 {M_number} To +91 {new_number} ✔ ")
    else :
     print("There is No Data Regarding This Mobile Number ✔")
  except Exception as e :
    print("The Occured Error is ",e)


def email_update() :
  print("Ok lets Update Email ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
     while True :
       # we have to solve an error in this seris of codes where i put wrong sql query 
       # i am not getting any error but still i had check and i  got tht i have written wrong sql query
       name = input("Enter Your Name : ").strip().title() 
       email = input("Enter Your Current Email : ").strip().lower()
       pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
       if re.match(pattern,email) :
         print("Ok Valid Email Type ✔")
         cursor.execute("SELECT * FROM doctors WHERE email = ?",(email,))
         row = cursor.fetchone()
         if row :
           print("Ok Email is Valid Now You Can Change Your Existing Email ✔")
           new_email = input("Enter New Email To Update : ").strip().lower()
           pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
           while True :
            if re.match(pattern,email) :
              cursor.execute("UPDATE doctors SET email = ? WHERE name = ?",(new_email,name))
              conn.commit()

              print("The Email Has Been Updated Succesfully ✔")

              break
            else :
              print("The Email Formate is wrong Please Try Again ✔ ")
         else :
           print("There is No Data With This Email Id ✔")

  except Exception as e :
    print("The Occured Error is ",e)



def speacilization_update() :
  print("Ok Lets Update Your Specilization ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    while True : 
     name = input("Enter Your Name : ").strip().title()
     specialization = input("Enter Your specialization : ").strip().title()
     cursor.execute("SELECT * FROM doctors WHERE name = ? AND specialization = ?",(name,specialization))
     rows = cursor.fetchall()
     for row in rows : 
      name_2 = (row["name"])
      if rows :
       print(f"Welcome - {name_2}! lets Change Your Specialization ✔")
       new_Specialization = input(f"{name_2} Enter Your New  Specialization : ").strip().title()
       cursor.execute("UPDATE doctors SET Specialization = ? WHERE name = ?",(new_Specialization,name))

       conn.commit()
       print("Ok New Specialization Has Been Updated Succesfully ✔")

       break
  except Exception as e :
    print("The Occured Error is :",e)
  
def age_update() :
  print("Ok Lets Update Your Age ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    while True :
      name = input("Enter Your Name : ").strip().title()
      age_1 = input("Enter Your Current Age").strip()
      if age_1.isdigit() and len(age_1) <= 67 :

       age = int(age_1)
       cursor.execute("SELECT * FROM doctors WHERE name = ? AND age = ?",(name,age))
       rows = cursor.fetchall()
       for row in rows :
         name_2 = (row["name"])
         if rows :
           print(f"Ok Welcome - {name_2}!")
           new_age = input("Enter New Age : ").strip()
           if new_age.isdigit() and new_age >= 25 and new_age <= 67 :
             print("OK its Valid AGE Formate ✔")
             cursor.execute("UPDATE doctors SET age = ? WHERE name = ?",(new_age,name))
             conn.commit()
             print(f"Ok - {name} Your Age Change From : {age} To {new_age} ✔")

         else :
           print("We Are Sorry,But There is No Data With Your Name and age Both Are Matches ✔")

      else :
        print("The Age is Not Valid ✔")
      
      break
  except Exception as e :
    print("The Occured Eror is ",e)




def serach_engine_hospital() :
  # in this hosptail engine user just need to entre their illness and our engine 
  # find best nearst hospital for them using open streat map api
  # current we will do dummy logic but the logic will repvent for logng time 
  # and later we will you open streatt map api
  print("Ok Here We Are In Hospital Search Engine ✔")
  illness = input("Enter Your Illness : ").strip().title()
  # dummy logic start


  # this logic totaly written by ai i have not writte a single code line in this section of code 
  # we have to imporve this code logic by 50% so we can make logic pure beaset

  # waht we do in editing of this code
  #1.) we will put the databse so we can access out of them
  #2/)and we will intorduce rapidfuzz libary so we can serch engine if they type not matched
   
  hospitals = {
    "City Hospital" : ["Flu","Cold","Fever","Cough"],
    "Green Valley Hospital" : ["Diabetes","Hypertension","Asthma"],
    "Sunrise Medical Center" : ["Fracture","Sprain","Injury"],
    "Riverdale Clinic" : ["Allergy","Skin Infection","Eczema"],
    "Mountainview Health" : ["Heart Disease","Stroke","Cholesterol"]
  }
  found_hospitals = []
  for hospital,specializations in hospitals.items() :
    if illness in specializations :
      found_hospitals.append(hospital)

  if found_hospitals :
    print(f"Here are the hospitals that specialize in treating {illness} :")
    for hospital in found_hospitals :
      print(f"- {hospital}")
  else :
    print(f"Sorry, we couldn't find any hospitals that specialize in treating {illness}.")
  # dummy logic end
  # later we will use open streat map api for that
  # we will use geopy library for that

# _________________________________________________________________________________________________________a
# and we will save the city data into data base for this type of locatin serch


def recomedation_engine() :
  print("OK lets Create A Recomdation Engine That Solve People Problem ✔")




def hospital_name_update() :
  print("Ok lets Update Hospital Name ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    while True :
      name = input("Enter Your Name : ").strip().title()
      hospital_name = input("Enter Your Hospital Name : ").strip().title()
      cursor.execute("SELECT * FROM doctors WHERE name = ? AND hospital_name = ?",(name,hospital_name))

      rows = cursor.fetchall()
      for row in rows : 
       name_2 = (row["name"])
       if rows :
        print(f"Welcome - {name_2}! lets Change Your Hospital Name ✔")
        new_hospital_name = input(f"{name_2} Enter Your New Hospital Name : ").strip().title()
        cursor.execute("UPDATE doctors SET hospital_name = ? WHERE name = ?",(new_hospital_name,name))

        conn.commit()
        print("Ok New Hospitle Name  Has Been Updated Succesfully ✔")

      break
  except Exception as e :
    print("The Occured Eror is ",e)
    

# _________________________________________________________________________________________________________

def doctor_update_profile() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  print("Ok lets Update Your Profile ✔")
  try :
    name = input("Enter Your Name : ").strip().title()
    password = pwinput.pwinput(prompt = "Enter Password To View Your Profile : ").strip().title()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM doctors WHERE name = ?AND password ?",(name,hash_password,))
    rows = cursor.fetchall()
    for row in rows :
     name_master = (row["name"])
     mobile_number = (row["mobile_number"])
     email = (row["email"])
     specilization = (row["specialization"])
     age = (row["age"])
     hospital_name = (row["hospital_name"])
    if rows :
     print("\nHere is Your Detail ✔\n")
     print(f"\nWelcome {name_master} \nMobile Number is : +91 {mobile_number} \nEmail id is : {email} \n{name_master} Specilization is : {specilization}\nThe AGE Of {name_master} is : {age} From : {hospital_name}\n")
     option = input("\nNow Please Select What Do You Want To Update : \n1.)Name \n2.)Mobile_number \n3.)Email \n4.)Specilization \n5.)AGE \n6.)Hospital Name \nYour Choice : ").strip()
     try :
       if option == "1" :
        name_update()
       elif option == "2" :
        mobile_number_update()
       elif option == "3" :
        email_update()
       elif option == "4" :
        speacilization_update()
       elif option == "5" :
         age_update()
       elif option == "6" :
         hospital_name_update()

       else :
        print("Please Try Valid Option ✔")
     except Exception as e :
      print("The Occured Error is ",e)

    else :
     print("No Doctor Data Found ✔")
   
  except Exception as e :
    print("The Occured Error is ",e)


def doctor_logout() :
  print("Ok lets Logout Session To Doctor ✅")
  # for this logic we will create logged_status colum where we will put 0 means loged in ,1 means loged out
  # when doctor try to logout we will store flag means we will update existing one  and click logout
  # and cancel all feature for doctor
  # and when doctor try to access feature we will check falg status which we have saved in DB
  # and if it s 1 we will say to doctor please login and if doctor denied to login 
  # close all feature for him and when he had done his login unlock all feature
  # that too easy task for me lets do it 
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    while True :
     option = input("\nAre You Sure Want To Log-Out \n1.)Yes \n2.)No \nYour Choice : ").strip()
     if option == "1" :
       print("Ok lets Log-Out ✅")
       # currently we are taking name to input for log out by checking name but when we create 
       # session.json than we will upgrade to without enter the name so remeber
       # and also we have to impliment logic copy of user name like when user regirster and entre the name
       # we will check in db and if its avalibal we will say to user that the user name is already exist please
       # try another user name so while log out or other thing if they had same user name the other person
       # data also will log out or same thing would happend for that 
       name = input("Enter Your Name To Log-Out : ").strip()
       cursor.execute("SELECT * FROM doctors WHERE name = ?",(name,))
       row = cursor.fetchone()
       if row :
         print("Ok You Are Valid User.Access Granted ✔")
         rows = cursor.fetchall()
         for row in rows :
          name_2 = (row["name"])
         if rows :
          logged_status = "1"
          cursor.execute("UPDATE doctors SET logged_status = ? WHERE name = ? ",(logged_status,name))
         
          print(f"{name_2} You Session Now Expired ✅")
          conn.commit()
          break
         else :
          print(f"There is No Active User Session with name OF : {name}! Please Try Again")
     elif option == "2" :
       print("OK No Problem if You Dont Want To Log-Out ✅")
       exit()
     else :
       print("Please Select valid Option ✔")
       
  except Exception as e :
    print("The Occured Error is ",e)



def add_doctor() :
  # logic detail - we are implimetaing this logic while asuming that when a doctor got register in x hospital
  # his/her data will store to doctors tabel now thie things is if the user doctor want to add more doctor
  # data for his hospital so if we mix his doctor and register doctor that will make biggest blunder 
  # becuae when we need reigister doctor report how we could find it when we mix it so be alert 
  # and create a seperate tabel that will coduct only taht data that a alredy cusotmer doctore want to add
  # new doctor so we can easlily define and if he want data he will put his hospital name and id and 
  # we will fetch the data form data base 
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
   
  print("Ok Lets Add Doctors ✔")
  try :
    while True :
      doctor_name = input("Enter Doctor Name : ").strip().title()
      if not doctor_name.isdigit() :
        print("Ok Vaild Doctor Name ✔")   

        break
      else :
        print("Not Valid Docotr Name ❌")   
    while True :
      hospital_name = input("Enter Hospital Name For Doctor (not : With This Hospital Name The Unique id will generate) : ").strip().title()
      pattern = r'^([A-Z][a-z]+)(\s[A-Z][a-z]+)*$'
      if re.match(pattern,hospital_name) :
        print("Ok Valid Hospital Name ✔")
        break
      else :
        print("Please Enter Valid Hospital Name ✔")
      
    while True :
      specialication = input("Enter Doctor Specialization : ").strip().title()
      pattern = r'^[A-Za-z\s]{3,50}$'
      if re.match(pattern,specialication) :
        print("Ok Valid Specialization ✔")
        break
      else :
        print("Please Enter Valid Specialization ✔")
    while True :
      m_number = input("Enter Doctor 10 Digit Mobile Number For Comunication & Message : +91 ").strip().title()
      pattern = r"^[6-9]\d{9}$"
      phone = int(m_number)
      if re.match(pattern,m_number) and len (m_number) == 10 :
        print("Ok Mobile Number Valided ✔")
        break
      else :
        print("Please Enter Valid Mobile Number ✔")
    while True :
      email = input("Enter Doctor Email ID (This Email ID Will Use For Comunication & Message) : ").strip().lower()
      pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
      if re.match(pattern,email) :
        print("Ok Email ID Valided ✔")
        break
      else :
        print("Please Enter Valid Email ID ✔")
    while True :
      print("Now You Will Get An Hospital Unique ID That Will Help To Find Your Hospital Doctor Easily ✔")
      short_id = unique_id.split("-")[0]
      hospital_id = short_id+"@"+hospital_name.replace(" ","").lower()
      print(f"Your Hospital Unique ID is : {hospital_id} \nPlease Note This ID For Future Use ✔")
      confirm_id = input("Please Confirm Your Hospital Unique ID : ").strip().lower()
      print(f"Your Hospital Unique ID is : {hospital_id} \nPlease Note This ID For Future Use ✔")
      if confirm_id == hospital_id :
        print("Ok Hospital ID Confirmed ✔")
        hash_id = hashlib.sha256(hospital_id.encode()).hexdigest()

        break
      else :
        print("Hospital ID Not Matched Please Try Again ✔")
    detail = {
      "name" : doctor_name,
      "hospital_name" : hospital_name,
      "specialization" : specialication,
      "mobile_number" : phone,
      "email" : email,
      "hospital_id" : hash_id,
      "time" : current_time
    }
    cursor.execute("""INSERT INTO hospital_doctors (name,hospital_name,specialization,mobile_number,email,hospital_id,time)
                   VALUES (?,?,?,?,?,?,?)""",(
      detail["name"],
      detail["hospital_name"],
      detail["specialization"],
      detail["mobile_number"],
      detail["email"],
      detail["hospital_id"],
      detail["time"]
    ))
    conn.commit()
    print(f"Doctor {doctor_name} Added Successfully To : {hospital_name} ✔")

  except Exception as e :
    print("The Occured Error is ",e)


def view_patients() :
  print("Ok Here We Are In View Patients Section ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    hospital_name = input("Enter Your Hospital Name To View Patients : ").strip().title()
    cursor.execute("SELECT * FROM patients WHERE hospital_name = ?",(hospital_name,))
    rows = cursor.fetchall()
    if rows :
      print(f"Here is The Patients List Of {hospital_name} ✔\n")
      for row in rows :
        name = (row["name"])
        mobile_number = (row["mobile_number"])
        email = (row["email"])
        age = (row["age"])
        print(f"Name: {name}, Mobile Number: {mobile_number}, Email: {email}, Age: {age} and illness : {row['illness']} and From Hospital : {row['hospital_name']}")
    else :
      print("No Patients Data Found ✔")
  except Exception as e :
    print("The Occured Error is ",e)



def add_patients() :
  print("Ok Here We Are In Add Patients Section ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    while True :
      name = input("Enter Patient Name : ").strip().title()
      pattern = r'^([A-Z][a-z]+)(\s[A-Z][a-z]+)*$'
      if re.match(pattern,name) :
        print("Ok Valid Patient Name ✔")
        break
      else :
        print("Not Valid Patient Name ❌")   
    while True :
      hospital_name = input("Enter Hospital Name Where Patient is Admitted : ").strip().title()
      pattern = r'^([A-Z][a-z]+)(\s[A-Z][a-z]+)*$'
      if re.match(pattern,hospital_name) :
        print("Ok Valid Hospital Name ✔")
        break
      else :
        print("Please Enter Valid Hospital Name ✔")
      
    while True :
      illness = input("Enter Patient Illness : ").strip().title()
      pattern = r'^[A-Za-z\s]{3,50}$'
      if re.match(pattern,illness) :
        print("Ok Valid Illness ✔")
        break
      else :
        print("Please Enter Valid Illness ✔")
    while True :
      m_number = input("Enter Patient 10 Digit Mobile Number For Comunication & Message : +91 ").strip().title()
      pattern = r"^[6-9]\d{9}$"
      phone = int(m_number)
      if re.match(pattern,m_number) and len (m_number) == 10 :
        print("Ok Mobile Number Valided ✔")
        break
      else :
        print("Please Enter Valid Mobile Number ✔")
    while True :
      email = input("Enter Patient Email ID (This Email ID Will Use For Comunication & Message) : ").strip().lower()
      pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
      if re.match(pattern,email) :
        print("Ok Email ID Valided ✔")
        break
      else :
        print("Please Enter Valid Email ID ✔")
    while True :
      age = input("Enter Patient Age : ").strip()
      if age.isdigit() and 1 <= int(age) <= 120 :
        age = int(age)
        print("Ok Age Valided ✔")
        break
      else :
        print("Please Enter Valid Age Between 1 to 120 ✔")

    detail = {
      "name" : name,
      "hospital_name" : hospital_name,
      "illness" : illness,
      "mobile_number" : phone,
      "email" : email,
      "age" : age,
      "time" : current_time
    }
    cursor.execute("""INSERT INTO patients (name,hospital_name,illness,mobile_number,email,age,time)
                   VALUES (?,?,?,?,?,?,?)""",(detail["name"],
                                                  detail["hospital_name"],
                                                  detail["illness"],
                                                  detail["mobile_number"],
                                                  detail["email"],
                                                  detail["age"],
                                                  detail["time"]
                                                  ))
    conn.commit()
    print(f"Patient {name} Added Successfully To : {hospital_name} ✔")


  except Exception as e :
    print("The Occured Error is ",e)


def assign_the_doctor() :
  # 0 mean doctor avalibal and 1 means doctor in unabalibal # and we are creating this function logic 
  # like that right now we are adding 15 doctor taht are not assigned yet and aftre addeding them
  # i will change logic of this functin and usrer will enter there illenss and and we will check that illenss
  # and docotr for that illenss and if doctor avalibal means 0 than we will assign the doctor if not 0 
  # we will not assign the doctor and say that for this illiness this doctor are busy
  # and we will add a option in docotr panel where if docotr got free they will make update in db 
  # taht nowthey are freee and the all time stamp will be checked and db will updatae and then with 
  # any one can docotr assign


  # we will keep alive this logic because we need to add 50 + doctors


# _____________________________________________________________________________________________________


  # and when we change the logic user haave to select thier hospital name and  illness type like kidey,cardiologist
  # if they put wrong name we will use rapidfuzz to get closet recomedation 
  # after select ing that we will check doctor list  and we will select from that 
  # and check doctor assign status if he assign we wills say wait for minute
  # when doctor got frree they have to say when they click on free ,the notification will pop up on
  # scrreen and say that this docotr is free form this department anyone want to go they can go



  #and later we will introduce token based system and doctor have to give the token to peoplwe 
  # we will use for loop for the give token to people doctor will give token by his romm in croweded day
  # if there is not crowed day there will automatic will assign like when doctor free the futher person
  # who had entred first at x hospital they can go
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  while True :
   print("OK lets Assing The Doctor ✔")

   enter = input("Enter Doctor Name : Dr. ").strip().title()
   specliti = input("Enter Doctor Speciazaiotn : ").strip().title()
   hospital_name = input ("Enter Hospital Name : ").strip().title()
   avalibal = '0'

   detail = {
    "doctor_name" : enter,
    "hospital_name" : hospital_name,
    "specailzation" : specliti,
    "avalibal" : avalibal,
    "time" : current_time
   }
   cursor.execute(""" INSERT INTO assigned_doctor (doctor_name,specailzation,hospital_name,avalibal,time)
                  VALUES (?,?,?,?,?)
                  
                  """,(detail["doctor_name"],
                       detail["specailzation"],
                       detail["hospital_name"],
                       detail["avalibal"],
                       detail["time"]))
   conn.commit()

   break
  print("The Doctor Succesfull Assigned ✔")

# i will  put the whole function category in a class so that we can get structure




class state_cancer() :
 
  def __init__ (self) :
    print("Ok Here We Go With Best Cancer Hospital For You ✅")
  
  def state_gujrat() :
    print("Ok lets Find Best Cancer Hospital For You In Gujrat ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    
    try :
     while True :
       select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
       if select == "1" :
         print("Ok Here is The Best 3 Cancer Hospital in Gujrat ✅")
         state_2 = "Gujrat"
         cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
         
         rows = cursor.fetchall()
         if rows :
           print("\nCongrates You Got The Best Hospital ✅\n")
           for idx,row in enumerate(rows,start=1):
             hospital_name,illness_type,hospital_rating,address,mobile_number = row
             print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

           option = input("\nDo You Want To Go With All Best Cancer Hospital in Gujrat ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
           if option == "1" :
             cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
             row_master = cursor.fetchall()
             if row_master :
               for idx,row_vector in enumerate(row_master,start=1) :
                 hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                 print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")
                 

    
           elif option == "2" :
             print("Ok No Problem Have A Nice Day ✅")
             exit()
           else :
             print("Please Select An Valid Option ✅")
           

         else :
           print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
       elif select == "2" :
         master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \nYour Choice : ").strip()
         if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Vadodara - Gujrat ✅")
            city = "Vadodara"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

         elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Ahemdabad - Gujrat ✅")
            city = "Ahemdabad"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

         elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Surat - Gujrat ✅")
            city = "Surat"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
         else :
            print("Please Select An Valid Option ✅")
       else :
          print("Please Select An Valid Option ✅")
      
       break
    except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_maharastra() :
    print("Ok lets Find Best Cancer Hospital For You in Maharashtra ✅")
    try :
     
     
      conn = sqlite3.connect(db_path)
      conn.row_factory = sqlite3.Row
      cursor = conn.cursor()

    
      
      while True :
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Cancer Hospital in Maharastra ✅")
            state_2 = "Maharastra"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
         
            rows = cursor.fetchall()
            if rows :
             print("\nCongrates You Got The Best Hospital in Maharastra ✅\n")
             for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

             option = input("\nDo You Want To Go With All Best Cancer Hospital in Maharastra ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
             if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")
                 

    
             elif option == "2" :
               print("Ok No Problem Have A Nice Day ✅")
               exit()
             else :
               print("Please Select An Valid Option ✅")
           

            else :
               print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
    
            break
          elif select == "2" :
           master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Mumbai \n2.)Pune \n3.)Nagpur \nYour Choice : ").strip()
           if master == "1" :
             print("Ok Here is The Best 3 Cancer Hospital For You in Mumbai - Maharashtra ✅")
             city = "Chennai"
             cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
             mobile = cursor.fetchall()
             for idx,lens in enumerate(mobile,start=1) :
               print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

           elif master == "2" :
             print("Ok Here is The Best 3 Cancer Hospital For You in Pune - Maharashtra ✅")
             city = "Madhurai"
             cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
             mobile = cursor.fetchall()
             for idx,lens in enumerate(mobile,start=1) :
               hospital_name,illness_type,hospital_rating,address,mobile_number = lens
               print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

           elif master == "3" :
             print("Ok Here is The Best 3 Cancer Hospital For You in Nagpur - Maharashtra ✅")
             city = "Nagpur"
             cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
             mobile = cursor.fetchall()
             for idx,lens in enumerate(mobile,start=1) :
               hospital_name,illness_type,hospital_rating,address,mobile_number = lens
               print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
           else :
             print("Please Select An Valid Option ✅")
          else :
            print("Please Select An Valid Option ✅")
      
          break
       

    except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_tamil_nadu() :
    print("Ok lets Find Best Cancer Hospital For You In Tamil Nadu ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try :
     while True :
        select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
        if select == "1" :
          print("Ok Here is The Best 3 Cancer Hospital in TamilNadu ✅")
          state_2 = "Tamilnadu"
          cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
         
          rows = cursor.fetchall()
          if rows :
            print("\nCongrates You Got The Best Hospital in Tamil Nadu ✅\n")
            for idx,row in enumerate(rows,start=1):
              hospital_name,illness_type,hospital_rating,address,mobile_number = row
              print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

            option = input("\nDo You Want To Go With All Best Cancer Hospital in Tamil Nadu ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
            if option == "1" :
              cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
              row_master = cursor.fetchall()
              if row_master :
                for idx,row_vector in enumerate(row_master,start=1) :
                  hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                  print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")
                 

    
            elif option == "2" :
               print("Ok No Problem Have A Nice Day ✅")
               exit()
            else :
               print("Please Select An Valid Option ✅")
           

          else :
               print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
    
          break
        elif select == "2" :
          master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Chennai \n2.)Madhurai \n3.)Coimbator \nYour Choice : ").strip()
          if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Chennai- Tamilnadu ✅")
            city = "Chennai"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city =  ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Madhurai - Tamilnadu ✅")
            city = "Madhurai"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Coimbator -Tamilnadu ✅")
            city = "Coimbator"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
             print("Please Select An Valid Option ✅")
        else :
            print("Please Select An Valid Option ✅")
        break
    except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_rajsthan() :
    print("Ok lets Find Best Cancer Hospital For You In Rajsthan ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try :
     while True :
       select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
       if select == "1" :
        print("Ok Here is The Best 3 Cancer Hospital in Rajshtahn ✅")
        state_2 = "Rajshtan"
        cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
         
        rows = cursor.fetchall()
        if rows :
          print("\nCongrates You Got The Best Hospital in Rajsthan ✅\n")
          for idx,row in enumerate(rows,start=1):
            hospital_name,illness_type,hospital_rating,address,mobile_number = row
            print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

          option = input("\nDo You Want To Go With All Best Cancer Hospital in Rajsthan ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
          if option == "1" :
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
            row_master = cursor.fetchall()
            if row_master :
              for idx,row_vector in enumerate(row_master,start=1) :
                hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")
                 

    
          elif option == "2" :
              print("Ok No Problem Have A Nice Day ✅")
              exit()
          else :
              print("Please Select An Valid Option ✅")
           

        else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
    
        break
       elif select == "2" :
          master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Jaipur \n2.)Udaipur \n3.)Chittodgadh \nYour Choice : ").strip()
          if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Jaipur - Rajsthan ✅")
            city = "Jaipur"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city =  ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Udaipur - Rajsthan ✅")
            city = "Udaipur"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Chittorgadh - Rajsthan ✅")
            city = "Chittorgadh"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
             print("Please Select An Valid Option ✅")
       else :
            print("Please Select An Valid Option ✅")
     
       break
    except Exception as e :
      print("Please Select An Valid Option ✅")

  def state_telngana() :
    print("Ok lets Find Best Cancer Hospital For You In Telngana ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try :
     while True :
        select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
        if select == "1" :
          print("Ok Here is The Best 3 Cancer Hospital in Telngana ✅")
          state_2 = "Tamilnadu"
          cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
         
          rows = cursor.fetchall()
          if rows :
            print("\nCongrates You Got The Best Hospital in Telngana ✅\n")
            for idx,row in enumerate(rows,start=1):
              hospital_name,illness_type,hospital_rating,address,mobile_number = row
              print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

            option = input("\nDo You Want To Go With All Best Cancer Hospital in Telngana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
            if option == "1" :
              cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
              row_master = cursor.fetchall()
              if row_master :
                for idx,row_vector in enumerate(row_master,start=1) :
                  hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                  print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")
                 

    
            elif option == "2" :
               print("Ok No Problem Have A Nice Day ✅")
               exit()
            else :
               print("Please Select An Valid Option ✅")
           

          else :
               print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
    
          break
        elif select == "2" :
          master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Hydrabad \n2.)Warangal \n3.)Karimnagar \nYour Choice : ").strip()
          if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Hydrabad- Telngana ✅")
            city = "Hydrabad"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city =  ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Warangal - Telngana ✅")
            city = "Warangal"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in  Karimnagar - Telngana ✅")
            city = "Karimnagar"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
             print("Please Select An Valid Option ✅")
        else :
            print("Please Select An Valid Option ✅")
               
    except Exception as e :
      print("Please Select An Valid Option ✅")

  def select_haryana() :
    print("Ok lets Find Best Cancer Hospital For You In Haryana ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try :
     while True :
        select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
        if select == "1" :
          print("Ok Here is The Best 3 Cancer Hospital in Haryana ✅")
          state_2 = "Haryana"
          cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
         
          rows = cursor.fetchall()
          if rows :
            print("\nCongrates You Got The Best Hospital in Haryana ✅\n")
            for idx,row in enumerate(rows,start=1):
              hospital_name,illness_type,hospital_rating,address,mobile_number = row
              print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

            option = input("\nDo You Want To Go With All Best Cancer Hospital in Haryana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
            if option == "1" :
              cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
              row_master = cursor.fetchall()
              if row_master :
                for idx,row_vector in enumerate(row_master,start=1) :
                  hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                  print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")
                 

    
            elif option == "2" :
               print("Ok No Problem Have A Nice Day ✅")
               exit()
            else :
               print("Please Select An Valid Option ✅")
           

          else :
               print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
    
          break
        elif select == "2" :
          master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Gurgaon \n2.)Faridabad \n3.)Chandigadh \nYour Choice : ").strip()
          if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Gurgaon - Haryana ✅")
            city = "Gurgaon"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city =  ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens 
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Faridabad - Haryana ✅")
            city = "Faridabad"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Chandigadh - Haryana ✅")
            city = "Chandigadh"
            cursor.execute("SELECT hospital_name,illenss_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
             print("Please Select An Valid Option ✅")
        else :
            print("Please Select An Valid Option ✅")
  
    except Exception as e :
      print("Please Select An Valid Option ✅")
  def more_differnt_hospital() :
    print("Ok lets Get More Hospital in Differnet City ✅")
    print("1.)\nHospital Name : Aiims Hospital \nLocation : Delhi \nillness Type : Cancer \nMobile Number : +91 854123697")
    print("2.)\nHospital Name : Master Life Care Hospital \nLocation : Madhyapradesh \nillness Type : Cancer \nMobile Number : +91 754122397")
    print("3.)\nHospital Name : Manav Hospital \nLocation : Kerla \nillness Type : Cancer \nMobile Number : +91 7541145397")
    print("4.)\nHospital Name : Amir Hospital \nLocation : Uttarpradesh \nillness Type : Cancer \nMobile Number : +91 7541145567")

    

    pass

watch = state_cancer()


class state_kideny() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  
  def __init__ (self) :
    print("Ok lets Find Best Kideny Hospital For You ✅ ")


  def state_gujrat() :
     print("Ok lets Find Best Kidney Hospital For You In Gujrat ✅")
     conn = sqlite3.connect(db_path)
     conn.row_factory = sqlite3.Row
     cursor = conn.cursor()
     try :
      while True :
        select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
        if select == "1" :
           print("Ok Here is The Best 3 Kidney Hospital in Gujrat ✅")
           state_2 = "Gujrat"
           cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
           rows = cursor.fetchall()
           if rows :
             print("\nCongrates You Got The Best Hospital ✅\n")
             for idx,row in enumerate(rows,start=1):
              hospital_name,illness_type,hospital_rating,address,mobile_number = row
              print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

             option = input("\nDo You Want To Go With All Best Cancer Hospital in Gujrat ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
             if option == "1" :
              cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
              row_master = cursor.fetchall()
              if row_master :
                for idx,row_vector in enumerate(row_master,start=1) :
                  hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                  print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

             elif option == "2" :
                print("Ok No Problem Have A Nice Day ✅")
                exit()
             else :
                print("Please Select An Valid Option ✅")
           

           else :
             print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
        elif select == "2" :
         master = input("\nSelect An City To Get Best Kidney Hospital \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \nYour Choice : ").strip()
         if master == "1" :
            print("Ok Here is The Best 3 Kidney Hospital For You in Vadodara - Gujrat ✅")
            city = "Vadodara"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

         elif master == "2" :
            print("Ok Here is The Best 3 Kidney Hospital For You in Ahemdabad - Gujrat ✅")
            city = "Ahemdabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

         elif master == "3" :
            print("Ok Here is The Best 3 Kidney Hospital For You in Surat - Gujrat ✅")
            city = "Surat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
         else :
            print("Please Select An Valid Option ✅")
    
      
      
     except Exception as e :
      print("Please Select An Valid Option ✅")




  def state_maharastra() :
     print("Ok lets Find Best Kidney Hospital For You In Maharastra ✅")
     try :
         while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Kidney Hospital in Maharastra ✅")
            state_2 = "Maharastra"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Kidney Hospital in Maharastra ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Mumbai \n2.)Pune \n3.)Nagpur \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Mumbai - Maharastra ✅")
            city = "Mumbai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Pune - Maharastra ✅")
            city = "Pune"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Nagpur - Maharastra ✅")
            city = "Nagpur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
     except Exception as e :
      print("Please Select An Valid Option ✅")

  def state_tamil_nadu() :
     print("Ok lets Find Best Kidney Hospital For You In Tamil Nadu ✅")
     try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Kidney Hospital in Tamilnadu ✅")
            state_2 = "Tamilnadu"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Kidney Hospital in Tamilnadu ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Chennai \n2.)Madhurai \n3.)Coimbator \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Chennai - Tamilnadu ✅")
            city = "Chennai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Madhurai - Tamilnadu ✅")
            city = "Madhurai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Coimbatore - Tamilnadu ✅")
            city = "Coimbatore"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
     except Exception as e :
      print("Please Select An Valid Option ✅")



  def state_rajsthan() :
     print("Ok lets Find Best Kidney Hospital For You In Rajsthan ✅")
     try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Kidney Hospital in Rajsthan ✅")
            state_2 = "Rajasthan"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Cancer Hospital in Rajasthan? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Jaipur \n2.)Udaipur \n3.)Ajmer \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Jaipur - Rajasthan ✅")
            city = "Jaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Udaipur - Rajasthan ✅")
            city = "Udaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Ajmer - Rajasthan ✅")
            city = "Ajmer"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
     except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_telngana() :
     print("Ok lets Find Best Kidney Hospital For You In Telngana ✅")
     try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Kidney Hospital in Telngana ✅")
            state_2 = "Telngana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Cancer Hospital in Telngana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Hyderabad \n2.)Secunderabad \n3.)Banjara Hills \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Hyderabad - Telngana ✅")
            city = "Hyderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Secunderabad - Telngana ✅")
            city = "Secunderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Cancer Hospital For You in Banjara Hills - Telngana ✅")
            city = "Banjara Hills"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
   
     except Exception as e :
      print("Please Select An Valid Option ✅")

  def select_haryana() :
     print("Ok lets Find Best Kidney Hospital For You In Haryana ✅")
     try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Kidney Hospital in Haryana ✅")
            state_2 = "Haryana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Cancer Hospital in Haryana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Kidney Hospital \n1.)Gurugram \n2.)Panchkula \n3.)Faridabad \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Kidney Hospital For You in Gurugram - Haryana ✅")
            city = "Gurugram"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Kidney Hospital For You in Panchkula - Haryana ✅")
            city = "Panchkula"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Kidney Hospital For You in Faridabad - Haryana ✅")
            city = "Faridabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM kidney_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      

     except Exception as e :
       print("Please Select An Valid Option ✅")

     pass


matrix = state_kideny()

class state_heart() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  
  def __init__ (self) :
    print("Ok lets Find Best Heart Hospital For You ✅")
  def state_gujrat() :
    print("Ok lets Find Best Heart Hospital For You In Gujrat ✅")
    
    try :
       while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Heart Hospital in Gujrat ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Heart Hospital in Gujrat ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Cancer Hospital \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Heart Hospital For You in Vadodara - Gujrat ✅")
            city = "Vadodara"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Heart Hospital For You in Ahemdabad - Gujrat ✅")
            city = "Ahemdabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Heart Hospital For You in Surat - Gujrat ✅")
            city = "Surat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")



  def state_maharastra() :
    print("Ok lets Find Best Heart Hospital For You In Maharashtra ✅")
    try :
       while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Heart Hospital in Maharashtra ✅")
            state_2 = "Maharashtra"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Heart Hospital in Maharashtra ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Heart Hospital \n1.)Mumbai\n2.)Pune  \n3.)Nagpur \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Heart Hospital For You in Mumbai - Maharashtra ✅")
            city = "Mumbai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Heart Hospital For You in Pune - Maharashtra ✅")
            city = "Pune"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Heart Hospital For You in Nagpur - Maharashtra ✅")
            city = "Nagpur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")

  def state_tamil_nadu() :
    print("Ok lets Find Best Heart Hospital For You In Tamil Nadu ✅")
    try :
       while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Heart Hospital in Tamilnadu✅")
            state_2 = "Tamilnadu"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Heart Hospital in Tamilnadu ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Heart Hospital \n1.)Chennai \n2.)Madhurai\n3.)Coimbator \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Heart Hospital For You in Chennai - Tamil Nadu ✅")
            city = "Chennai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Heart Hospital For You in Madhurai - Tamil Nadu ✅")
            city = "Madhurai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Heart Hospital For You in Coimbatore - Tamil Nadu ✅")
            city = "Coimbatore"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")

   

  def state_rajsthan() :
    print("Ok lets Find Best Heart Hospital For You In Rajsthan ✅")
    try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Heart Hospital in Rajasthan ✅")
            state_2 = "Rajasthan"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Heart Hospital in Rajasthan ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Heart Hospital \n1.)Jaipur \n2.)Udaipur \n3.)Ajmer \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Heart Hospital For You in Jaipur - Rajasthan ✅")
            city = "Jaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Heart Hospital For You in Udaipur - Rajasthan ✅")
            city = "Udaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Heart Hospital For You in Ajmer - Rajasthan ✅")
            city = "Ajmer"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
     
     

  def state_telngana() :
    print("Ok lets Find Best Heart Hospital For You In Telngana ✅")
    try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Heart Hospital in Telngana ✅")
            state_2 = "Telngana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Heart Hospital in Telangana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Heart Hospital \n1.)Hyderabad \n2.)Secunderabad \n3.)Banjara Hills \nYour Choice : ").strip()

           if master == "1" :
            print("Ok Here is The Best 3 Heart Hospital For You in Hyderabad - Telangana ✅")
            city = "Hyderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Heart Hospital For You in Secunderabad - Telangana ✅")
            city = "Secunderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Heart Hospital For You in Banjara Hills - Telangana ✅")
            city = "Banjara Hills"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")


  def select_haryana() :
    print("Ok lets Find Best Heart Hospital For You In Haryana ✅")
    try :
       while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Heart Hospital in Haryana ✅")
            state_2 = "Haryana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Heart Hospital in Haryana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Heart Hospital \n1.)Gurugram \n2.)Faridabad \n3.)Panchkula \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Heart Hospital For You in Gurugram - Haryana ✅")
            city = "Gurugram"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Heart Hospital For You in Faridabad - Haryana ✅")
            city = "Faridabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Heart Hospital For You in Panchkula - Haryana ✅")
            city = "Panchkula"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM heart_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")


    pass

space = state_heart()

class state_neurology() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  def __init__ (self) :
    print("Ok lets Find Best Neurology Hospital For You ✅")

  def state_gujrat() :
    print("Ok lets Find Best Neurology Hospital For You In Gujrat ✅")
    
    try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Neurology Hospital in Gujrat ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Neurology Hospital in Gujrat ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Neurology Hospital \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Vadodara - Gujrat ✅")
            city = "Vadodara"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Ahemdabad - Gujrat ✅")
            city = "Ahemdabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Surat - Gujrat ✅")
            city = "Surat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
    
     


  def state_maharastra() :
    print("Ok lets Find Best Neurology Hospital For You In Maharashtra ✅")
    try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Neurology Hospital in Maharashtra ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Neurology Hospital in Maharashtra ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Neurology Hospital \n1.)Mumbai \n2.)Pune \n3.)Nagpur \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Mumbai - Maharashtra ✅")
            city = "Mumbai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Pune - Maharashtra ✅")
            city = "Pune"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Nagpur - Maharashtra ✅")
            city = "Nagpur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")



  def state_tamil_nadu() :
    print("Ok lets Find Best Neurology Hospital For You In Tamil Nadu ✅")
    try :
      while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Neurology Hospital in Tamilnadu ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Neurology Hospital in Tamilnadu ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Neurology Hospital \n1.)Chennai \n2.)Madhurai \n3.)Coimbatore \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Chennai - Tamilnadu ✅")
            city = "Chennai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Madhurai - Tamilnadu ✅")
            city = "Madhurai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Coimbatore - Tamilnadu ✅")
            city = "Coimbatore"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
   


  def state_rajsthan() :
    print("Ok lets Find Best Neurology Hospital For You In Rajsthan ✅")
    try :
     while True :
       
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Neurology Hospital in Rajshthan ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Neurology Hospital in Rajshthan ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Neurology Hospital \n1.)Jaipur \n2.)Udaipur \n3.)Ajmer \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Jaipur - Rajasthan ✅")
            city = "Jaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Udaipur - Rajasthan ✅")
            city = "Udaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Ajmer - Rajasthan ✅")
            city = "Ajmer"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
 
     

  def state_telngana() :
    print("Ok lets Find Best Neurology Hospital For You In Telngana ✅")
    try :
     while True :
       
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Neurology Hospital in Telngana ✅")
            state_2 = "Telngana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Neurology Hospital in Telngana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Neurology Hospital \n1.)Hyderabad \n2.)Secunderabad \n3.)Banjara Hills \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Hyderabad - Telangana ✅")
            city = "Hyderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Secunderabad - Telangana ✅")
            city = "Secunderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Banjara Hills - Telangana ✅")
            city = "Banjara Hills"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
     print("Please Select An Valid Option ✅")


  def select_haryana() :
    print("Ok lets Find Best Neurology Hospital For You In Haryana ✅")
    try :
     while True :
       
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Neurology Hospital in Haryana ✅")
            state_2 = "Haryana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Neurology Hospital in Haryana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Neurology Hospital \n1.)Gurugram \n2.)Faridabad \n3.)Panchkula \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Gurugram - Haryana ✅")
            city = "Gurugram"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Faridabad - Haryana ✅")
            city = "Faridabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Neurology Hospital For You in Panchkula - Haryana ✅")
            city = "Panchkula"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM neurology_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
 



    pass
vector = state_neurology()

class state_orthopadic() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  def __init__ (self) :
    print("Ok lets Find Best Orthopadic Hospital For You ✅")

  def state_gujrat() :
    print("Ok lets Find Best Orthodpadic Hospital For You In Gujrat ✅")
    
    try :
     while True :
       
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Orthopadic Hospital in Gujrat ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Orthopadic Hospital in Gujrat ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Orthopadic Hospital \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Orthopadic Hospital For You in Vadodara - Gujrat ✅")
            city = "Vadodara"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Orthopadic Hospital For You in Ahemdabad - Gujrat ✅")
            city = "Ahemdabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Orthopadic Hospital For You in Surat - Gujrat ✅")
            city = "Surat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
 


  def state_maharastra() :
    print("Ok lets Find Best Orthodpadic Hospital For You In Maharashtra ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Orthopadic Hospital in Maharashtra ✅")
            state_2 = "Maharashtra"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Orthopadic Hospital in Maharashtra ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Orthopadic Hospital \n1.)Mumbai\n2.)Pune \n3.)Nagpur \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Orthopadic Hospital For You in Mumbai - Maharashtra ✅")
            city = "Mumbai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Orthopadic Hospital For You in Pune - Maharashtra ✅")
            city = "Pune"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Orthopadic Hospital For You in Nagpur - Maharashtra ✅")
            city = "Nagpur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
     


  def state_tamil_nadu() :
    print("Ok lets Find Best Orthodpadic Hospital For You In Tamil Nadu ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Orthopadic Hospital in Tamilnadu ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Orthopadic Hospital in Tamilnadu ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Orthopedic Hospital \n1.)Chennai \n2.)Madhurai \n3.)Coimbatore \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Chennai - Tamil Nadu ✅")
            city = "Chennai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Madhurai - Tamil Nadu ✅")

            city = "Madhurai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Coimbatore - Tamil Nadu ✅")
            city = "Coimbatore"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_rajsthan() :
    print("Ok lets Find Best Orthodpadic Hospital For You In Rajsthan ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Orthopedic Hospital in Rajasthan ✅")
            state_2 = "Rajasthan"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Orthopedic Hospital in Rajasthan ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Orthopedic Hospital \n1.)Jaipur \n2.)Udaipur \n3.)Ajmer \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Jaipur - Rajasthan ✅")
            city = "Jaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Udaipur - Rajasthan ✅")
            city = "Udaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Ajmer - Rajasthan ✅")
            city = "Ajmer"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")

  def state_telngana() :
    print("Ok lets Find Best Orthopedic Hospital For You In Telngana ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Orthopedic Hospital in Telngana ✅")
            state_2 = "Telngana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Orthopedic Hospital in Telngana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Orthopedic Hospital \n1.)Hyderabad\n2.)Secunderabad\n3.)Banjara Hills \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Hyderabad - Telngana ✅")
            city = "Hyderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Secunderabad - Telngana ✅")
            city = "Secunderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Banjara Hills - Telngana ✅")
            city = "Banjara Hills"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
    

  def select_haryana() :
    print("Ok lets Find Best Orthodpadic Hospital For You In Haryana ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Orthopedic Hospital in Haryana ✅")
            state_2 = "Haryana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Orthopedic Hospital in Haryana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Orthopedic Hospital \n1.)Gurugram \n2.)Faridabad \n3.)Panchkula \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Gurugram - Haryana ✅")
            city = "Gurugram"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Faridabad - Haryana ✅")
            city = "Faridabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Orthopedic Hospital For You in Panchkula - Haryana ✅")
            city = "Panchkula"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM orthopadic_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")


    pass
master = state_orthopadic()


class state_eye() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  def __init__ (self) :
    print("Ok lets Find Best Eye Hospital For You ✅")
  def state_gujrat() :
    print("Ok lets Find Best Eye Hospital For You In Gujrat ✅")
    
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Eye Hospital in Gujrat ✅")
            state_2 = "Gujrat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Eye Hospital in Gujrat ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Eye Hospital \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Eye Hospital For You in Vadodara - Gujrat ✅")
            city = "Vadodara"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Eye Hospital For You in Ahemdabad - Gujrat ✅")
            city = "Ahemdabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Eye Hospital For You in Surat - Gujrat ✅")
            city = "Surat"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")



  def state_maharastra() :
    print("Ok lets Find Best Eye Hospital For You In Maharashtra ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Eye Hospital in Maharashtra ✅")
            state_2 = "Maharashtra"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Eye Hospital in Maharashtra ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Eye Hospital \n1.)Mumbai \n2.)Pune \n3.)Nagpur \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Eye Hospital For You in Mumbai - Maharashtra ✅")
            city = "Mumbai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Eye Hospital For You in Pune - Maharashtra ✅")
            city = "Pune"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Eye Hospital For You in Nagpur - Maharashtra ✅")
            city = "Nagpur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_tamil_nadu() :
    print("Ok lets Find Best Eye Hospital For You In Tamil Nadu ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Eye Hospital in Tamil Nadu ✅")
            state_2 = "Tamil Nadu"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Eye Hospital in Tamil Nadu ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Eye Hospital \n1.)Chennai \n2.)Madurai \n3.)Coimbatore \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Eye Hospital For You in Chennai - Tamil Nadu ✅")
            city = "Chennai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Eye Hospital For You in Madhurai - Tamil Nadu ✅")
            city = "Madhurai"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Eye Hospital For You in Coimbatore - Tamil Nadu ✅")
            city = "Coimbatore"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")



  def state_rajsthan() :
    print("Ok lets Find Best Eye Hospital For You In Rajsthan ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Eye Hospital in Rajasthan ✅")
            state_2 = "Rajasthan"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Eye Hospital in Rajasthan ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Eye Hospital \n1.)Jaipur \n2.)Udaipur \n3.)Ajmer \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Eye Hospital For You in Jaipur - Rajasthan ✅")
            city = "Jaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Eye  Hospital For You in Udaipur - Rajasthan ✅")
            city = "Udaipur"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Eye Hospital For You in Ajmer - Rajasthan ✅")
            city = "Ajmer"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
       print("Please Select An Valid Option ✅")
    

  def state_telngana() :
    print("Ok lets Find Best Eye Hospital For You In Telngana ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Eye Hospital in Telangana ✅")
            state_2 = "Telangana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Eye Hospital in Telangana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Eye Hospital \n1.)Hyderabad \n2.)Secunderabad \n3.)Banjara Hills \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Eye Hospital For You in Hyderabad - Telangana ✅")
            city = "Hyderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ?   ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Eye Hospital For You in Secunderabad - Telangana ✅")
            city = "Secunderabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM cancer_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Eye Hospital For You in Banjara Hills - Telangana ✅")
            city = "Banjara Hills"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")


  def select_haryana() :
    print("Ok lets Find Best Eye Hospital For You In Haryana ✅")
    try :
     while True :
          conn = sqlite3.connect(db_path)
          conn.row_factory = sqlite3.Row
          cursor = conn.cursor()
   
          select = input("\nSelect An Option \n1.)Search Hospital in Your State \n2.)Need AN City To Get The Hospital \nYour Choice : ").strip()
          if select == "1" :
            print("Ok Here is The Best 3 Eye Hospital in Haryana ✅")
            state_2 = "Haryana"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ? ORDER BY hospital_rating DESC LIMIT 3",(state_2,))
            rows = cursor.fetchall()
            if rows :
              print("\nCongrates You Got The Best Hospital ✅\n")
              for idx,row in enumerate(rows,start=1):
               hospital_name,illness_type,hospital_rating,address,mobile_number = row
               print(f"{idx} 🏥 {hospital_name} | {illness_type} | ⭐{hospital_rating} | 📍 {address} | 📱 +91 {mobile_number}")

              option = input("\nDo You Want To Go With All Best Eye Hospital in Haryana ? \n1.)Yes \n2.)No \nYour Choice : ").strip()
              if option == "1" :
               cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE state = ?",(state_2,))
               row_master = cursor.fetchall()
               if row_master :
                 for idx,row_vector in enumerate(row_master,start=1) :
                   hospital_name,illness_type,hospital_rating,address,mobile_number = row_vector
                   print(f"{idx} \nHospital Name : {hospital_name}  \nillness Type : {illness_type} \nHospital Rating : {hospital_rating} \nHospital Address : {address} \nMobile Number :  +91 {mobile_number}")

              elif option == "2" :
                 print("Ok No Problem Have A Nice Day ✅")
                 exit()
              else :
                 print("Please Select An Valid Option ✅")
           

            else :
              print("Sorry No Hospital Found Right Now Please Select Valid State ✅")
          elif select == "2" :
           master = input("\nSelect An City To Get Best Eye Hospital \n1.)Gurugram\n2.)Faridabad \n3.)Panchkula \nYour Choice : ").strip()
           if master == "1" :
            print("Ok Here is The Best 3 Eye Hospital For You in Gurugram - Haryana ✅")
            city = "Gurugram"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "2" :
            print("Ok Here is The Best 3 Eye Hospital For You in Faridabad - Haryana ✅")
            city = "Faridabad"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")

          elif master == "3" :
            print("Ok Here is The Best 3 Eye Hospital For You in Panchkula - Haryana ✅")
            city = "Panchkula"
            cursor.execute("SELECT hospital_name,illness_type,hospital_rating,address,mobile_number FROM eye_hospital WHERE city = ? ORDER BY hospital_rating DESC LIMIT 3",(city,))
            mobile = cursor.fetchall()
            for idx,lens in enumerate(mobile,start=1) :
              hospital_name,illness_type,hospital_rating,address,mobile_number = lens
              print(f"{idx} \nHospital Name : {hospital_name} \nillness Type : {illness_type}\nHospital Rating : {hospital_rating} \nAddress : {address} \n6.) Mobile Number : +91 {mobile_number}")
          else :
            print("Please Select An Valid Option ✅")
    
      
    except Exception as e :
      print("Please Select An Valid Option ✅")
      

    pass


finder  = state_eye()


# later we will use the open steet map api which can help us to locate the cusotmer 
# location at form location we can suggest the hospital or clinic behalf on what they select 


class ClinicFinderGujrat:

  def __init__ (self) :
    print("OK lets Find Best Clinic For You in Gujrat ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
  def vadodara_clinic() :
    print("Ok lets Find Best Clinic in Vadodara For You ✅")
    city = "Vadodara"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))

    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

    

  def ahemdabad_clinic() :
   print("Ok lets Find Best Clinic in Ahemdabad For You ✅")
   city = "Ahemdabad"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")
      




  def surat_clinic() :
    print("Ok lets Find Best Clinic in Surat For You ✅")
    city = "Surat"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def gandhi_nagar_clinic() :
    print("Ok lets Find Best Clinic in Gandhi Nagar For You ✅")
    city = "Gandhi Nagar"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")



  def junagadh_clinic() :
    print("Ok lets Find Best Clinic in JunaGadh For You ✅")
    city = "Junagadh"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")




clinic_gujrat =  ClinicFinderGujrat()

class ClinicFinderMaharastra:
  def __init__ (self) :
    print("OK lets Find Best Clinic in Maharastra ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
  def mumbai_clinic() :
    print("Ok lets Find Best Clinic For You in Mumbai ✅")
    city = "Mumbai"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def pune_clinic() :
    print("Ok lets Find Best Clinic For You in Pune ✅")
    city = "Pune"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")


  def nagpur_clinic() :
    print("Ok lets Find Best Clinic For You in Nagpur ✅")
    city = "Nagpur"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def navi_mumbai_clinic() :
    print("Ok lets Find Best Clinic For You in Navi Mumbai ✅")
    city = "Navi Mumbai"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def thane_clinic() :
    print("Ok lets Find Best Clinic For You in Thane ✅")
    city = "Thane"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def aurangabad_clinic() :
    print("Ok lets Find Best Clinic For You in Aurangabad ✅")
    city = "Aurangabad"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

    pass
 


clinic_maharastra = ClinicFinderMaharastra()

class ClinicFinderTamilnadu:
  def __init__ (self) :
    print("OK lets Find Best Clinic in Tamilnadu ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

  def chennai_clinic():
    print("Ok lets Find Best Clinic in Chennai ✅")
    city = "Chennai"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")




  def madhurai_clinic() :
    print("Ok lets Find Best Clinic in Madhurai ✅")
    city = "Madhurai"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")


    
  def coimbatore_clinic() :
    print("Ok lets Find Best Clinic in Coimbatore ✅")
    city = "Coimbatore"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def salem_clinic() :
    print("Ok lets Find Best Clinic in Salem ✅")
    city = "Salem"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def triuvchupalli_clinic() :
    print("Ok lets Find Best Clinic in Triuvchupalli ✅")
    city = "Triuvchupalli"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall() 
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

    pass


clinic_tamilnadu = ClinicFinderTamilnadu()



class ClinicFinderTelngana:
  def __init__ (self) :
    print("OK lets Find Best Clinic in Telngana ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
  def hyedarabad_clinic():
    print("OK lets Find Best Clinic in Hyderabad ✅")
    city = "Hyderabad"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")



  def secundarabad_clinic() :
    print("OK lets Find Best Clinic in Secundarabad ✅")
    city = "Secundarabad"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def banajar_hills_clinic() :
    print("OK lets Find Best Clinic in Banjara Hills ✅")
    city = "Banjara Hills"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def karimnagar_clinic() :
    print("OK lets Find Best Clinic in Karimnagar ✅")
    city = "Karimnagar"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

  def wraangle_clinic() :
    print("OK lets Find Best Clinic in Wraangle ✅")
    city = "Wraangle"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

    pass

  

 clinic_telngana = ClinicFinderTelngana()



class ClinicFinderRajshthan:
  def __init__ (self) :
    print("OK lets Find Best  Clinic in Rajsthan ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
  def jaipur_clinic() :
    print("Ok lets Find Best Clinic in Jaipur ✅ ")
    city = "Jaipur"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")




  def udaipur_clinic() :
    print("Ok lets Find Best Clinic in Udaipur ✅ ")
    city = "Udaipur"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")




  def ajmer_clinic():
    print("Ok lets Find Best Clinic in Ajmer ✅ ")
    city = "Ajmer"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")




  def kota_clinic() :
    print("Ok lets Find Best Clinic in Kota ✅ ")
    city = "Kota"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")  




  def bikaner_clinic() :
    print("Ok lets Find Best Clinic in Bikaner ✅ ")
    city = "Bikaner"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")


  def jaislmer_clinic() :
    print("Ok lets Find Best Clinic in Jaislmer ✅ ")
    city = "Jaislmer"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")
    pass





clinic_rajshtan = ClinicFinderRajshthan()




class ClinicFinderHaryana:
  def __init__ (self) :
    print("OK lets Find Best Nearest Clinic in Haryana ✅")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
  def gurugram_clinic() :
    print("Ok lets Find Best Clinic in Gurugram ✅ ")
    city = "Gurugram"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")


  def rohtak_clinic() :
    print("Ok lets Find Best Clinic in Rohtak ✅ ")
    city = "Rohtak"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")


  def faridabad_clinic() :
    print("Ok lets Find Best Clinic in Faridabad ✅ ")
    city = "Faridabad"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")


  def panchkula_clinic() :
    print("Ok lets Find Best Clinic in Panchkula ✅ ")
    city = "Panchkula"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")


  def gurgaon_clinic() :
    print("Ok lets Find Best Clinic in Gurgaon ✅ ")
    city = "Gurgaon"
    cursor.execute("SELECT clinic_name, illness_type, clinic_rating, address, mobile_number FROM clinic WHERE city = ? ORDER BY clinic_rating DESC LIMIT 3",(city,))
    clinics = cursor.fetchall()
    for idx, clinic in enumerate(clinics, start=1) :
      clinic_name, illness_type, clinic_rating, address, mobile_number = clinic
      print(f"{idx} \nClinic Name : {clinic_name} \nIllness Type : {illness_type}\nClinic Rating : {clinic_rating} \nAddress : {address} \nMobile Number : +91 {mobile_number}")

    pass



clinic_haryana = ClinicFinderHaryana()



class state_clinic_doctor() :
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  def __init__ (self) :
    print("OK lets Find Best Nearest Clinic ✅")
  def state_gujrat() :
    print("Ok lets Find Best Nearest Clinic For You In Gujrat ✅")
    
    try :
     while True :
  
       city = input("\nEnter Your City Name in Gujrat \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \n4.)Jamnagar \n5.)Junagadh \n6.)Gandhi Nagar \nYour Choice : ").strip()
       if city == "1" :
        clinic_gujrat.vadodara_clinic()
         
         break
       elif city == "2" :
         clinic_gujrat.ahemdabad_clinic()
         break
       elif city == "3" :
         clinic_gujrat.surat_clinic()
         break
       elif city == "4" :
         clinic_gujrat.jamnagar_clinic()
         break
       elif city == "5" :
         clinic_gujrat.junagadh_clinic()
         break
       elif city == "6" :
         clinic_gujrat.gandhi_nagar_clinic()
         break
       else :
         print("Please Select An Valid Option ✅")
       break
    except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_maharastra() :
    print("Ok lets Find Best Nearest Clinic For You In Maharashtra ✅")
    try :
     while True :

       city = input("\nEnter Your City Name in Maharastra \n1.)Mumbai \n2.)Nagpur \n3.)Pune \n4.)Navi Mumbai \n5.)Thane \n6.)Aurangabad \nYour Choice : ").strip()
       if city == "1" :
        clinic_maharastra.mumbai_clinic()
         break
       elif city == "2" :
         clinic_maharastra.nagpur_clinic()
         break
       elif city == "3" :
         clinic_maharastra.pune_clinic()
         break
       elif city == "4" :
        clinic_maharastra.navi_mumbai_clinic()
         break
       elif city == "5" :
         clinic_maharastra.thane_clinic()
         break
       elif city == "6" :
         clinic_maharastra.aurangabad_clinic()
         break
       else :
         print("Please Select An Valid Option ✅")
         break
 

    except Exception as e :
      print("Please Select An Valid Option ✅")

  def state_tamil_nadu() :
    print("Ok lets Find Best Nearest Clinic For You In Tamil Nadu ✅")
    try :
     while True :
       city = input("\nEnter Your City Name in Tamil Nadu \n1.)Chennai \n2.)Madhurai \n3.)Coimbatore \n4.)Salem\n5.)Triuvchupalli  \nYour Choice : ").strip()
       if city == "1" :
         clinic_tamilnadu.chennai_clinic()
         break
       elif city == "2" :
         clinic_tamilnadu.madhurai_clinic()
         break
       elif city == "3" :
         clinic_tamilnadu.coimbatore_clinic()
         break
       elif city == "4" :
         clinic_tamilnadu.salem_clinic()
         break
       elif city == "5" :
         clinic_tamilnadu.triuvchupalli_clinic()
         break
   
       else :
         print("Please Select An Valid Option ✅")
         break

    except Exception as e :
      print("Please Select An Valid Option ✅")


  def state_rajsthan() :
    print("Ok lets Find Best Nearest Clinic For You In Rajsthan ✅")
    try :
      while True :
        city = input("\nEnter Your City Name in Rajsthan \n1.)Jaipur \n2.)Udaipur \n3.)Ajmer \n4.)Kota \n5.)Jaislmer\n6.)Bikaner  \nYour Choice : ").strip()
        if city == "1" :
          clinic_rajshtan.jaipur_clinic()

          break
        elif city == "2" :
         clinic_rajshtan.udaipur_clinic()
          break
        elif city == "3" :
          clinic_rajshtan.ajmer_clinic()
          break
        elif city == "4" :
         clinic_rajshtan.kota_clinic()
          break
        elif city == "5" :
          clinic_rajshtan.jaislmer_clinic()
        elif city == "6" :
          clinic_rajshtan.bikaner_clinic()
    
        else :
          print("Please Select An Valid Option ✅")
          break

    except Exception as e :
      print("Please Select An Valid Option ✅")



  def state_telngana() :
    print("Ok lets Find Best Nearest Clinic For You In Telngana ✅")
    try :
     while True :
       city = input("\nEnter Your City Name in Telngana \n1.)Hyderabad \n2.)Secundarabad \n3.)Karimnagar \n4.)Banjara Hills \n5.)Wranngle \nYour Choice : ").strip()
       if city == "1" :
          clinic_telngana.hyderabad_clinic()
          break
       elif city == "2" :
          clinic_telngana.secundarabad_clinic()
          break
       elif city == "3" :
         clinic_telngana.karimnagar_clinic()
          break
       elif city == "4" :
          clinic_telngana.banajar_hills_clinic()
          break
       elif city == "5" :
         clinic_telngana.warrangle_clinic()
          break
       
       else :
          print("Please Select An Valid Option ✅")
          break
    
  
    except Exception as e :
      print("Please Select An Valid Option ✅")

  def select_haryana() :
    print("Ok lets Find Best Nearest Clinic  For You In Haryana ✅")
    try :
     while True :
       city = input("\nEnter Your City Name in Haryana \n1.)Gurugram \n2.)Rohtak \n3.)Panchkula \n4.)Faridabad \n5.)Gurgaon  \nYour Choice : ").strip()
       if city == "1" :
          clinic_haryana.gurugram_clinic()
          break
       elif city == "2" :
          clinic_haryana.rohtak_clinic()
          break
       elif city == "3" :
          clinic_haryana.panchkula_clinic()
          break
       elif city == "4" :
          clinic_haryana.faridabad_clinic()
          break
       elif city == "5" :
        clinic_haryana.gurgaon_clinic()
        break
      
       else :
          print("Please Select An Valid Option ✅")
          break
  
    except Exception as e :
      print("Please Select An Valid Option ✅")

    pass
  

  



def caner_hospital() :
  print("Ok Lets Find Best cancer Hospital ✅")
  try :
    while True :
      state = input("\nSelect An Option \n1.)Gujrat \n2.)Maharashtra \n3.)Tamil Nadu \4.)Rajsthan \n5.)Telngana \n6.)Haryana \nYour Choice :  ").strip().title()
      if state == "1" :
       
        watch.state_gujrat()
      elif state == "2":
       
        watch.state_maharastra()

      elif state == "3" :
        
        watch.state_tamil_nadu()

      elif state == "4" :
        watch.state_rajasthan()

      elif state == "5" :
      
       watch.state_telngana()

      elif state == "6" :
        
        watch.state_haryana()
      break

  except Exception as e :
    print("Please Enter The Valid Detail ✅")


def kidney_hospital() :
  print("Ok Lets Find Best Kidney Hospital ✅")
  try :
    while True :
      state = input("\nSelect An Option \n1.)Gujrat \n2.)Maharashtra \n3.)Tamil Nadu \4.)Rajsthan \n5.)Telngana \n6.)Hariyana \nYour Choice :  ").strip().title()
      if state == "1" :
        
        matrix.state_gujrat()
      elif state == "2":
       
        matrix.state_maharastra()

      elif state == "3" :
        
        matrix.state_tamil_nadu()

      elif state == "4" :
          
          matrix.state_rajasthan()

      elif state == "5" :
       
       matrix.state_telngana()

      elif state == "6" :
        
        matrix.state_haryana()
      break

  except Exception as e :
    print("Please Enter The Valid Detail ✅")


def heart_hospital() :
  print("Ok Lets Find Best Heart Hospital ✅")
  try :
    while True :
      state = input("\nSelect An Option \n1.)Gujrat \n2.)Maharashtra \n3.)Tamil Nadu \4.)Rajsthan \n5.)Telngana \n6.)Hariyana \nYour Choice :  ").strip().title()
      if state == "1" :
        
        space.state_gujrat()
      elif state == "2":
       
        space.state_maharastra()

      elif state == "3" :
       
        space.state_tamil_nadu()

      elif state == "4" :
          
          space.state_rajasthan()

      elif state == "5" :
      
       space.state_telngana()

      elif state == "6" :
       
        space.state_haryana()
      break

  except Exception as e :
    print("Please Enter The Valid Detail ✅")



def neurology_hospital() :
  print("Ok Lets Find Best Neurology Hospital ✅")
  try :
    while True :
      state = input("\nSelect An Option \n1.)Gujrat \n2.)Maharashtra \n3.)Tamil Nadu \4.)Rajsthan \n5.)Telngana \n6.)Hariyana \nYour Choice :  ").strip().title()
      if state == "1" :
        
        vector.state_gujrat()
      elif state == "2":
        
        vector.state_maharastra()
      elif state == "3" :
        
        vector.state_tamil_nadu()

      elif state == "4" :
          
          vector.state_rajasthan()

      elif state == "5" :
       
       vector.state_telngana()

      elif state == "6" :
        
        vector.state_haryana() 
      break

  except Exception as e :
    print("Please Enter The Valid Detail ✅")



def orthopadic_hospital() :
  print("Ok Lets Find Best Orthopadic Hospital ✅")
  try :
    while True :
      state = input("\nSelect An Option \n1.)Gujrat \n2.)Maharashtra \n3.)Tamil Nadu \4.)Rajsthan \n5.)Telngana \n6.)Hariyana \nYour Choice :  ").strip().title()
      if state == "1" :
        
        master.state_gujrat()

      elif state == "2":
        
        master.state_maharastra()

      elif state == "3" :
      
        master.state_tamil_nadu()

      elif state == "4" :
       
          master.state_rajasthan()

      elif state == "5" :
      
       master.state_telngana()

      elif state == "6" :
        
        master.state_haryana()
      break

  except Exception as e :
    print("Please Enter The Valid Detail ✅")


def eye_hospital() :
  print("Ok Lets Find Best Eye Hospital ✅")
  try :
    while True :
      state = input("\nSelect An Option \n1.)Gujrat \n2.)Maharashtra \n3.)Tamil Nadu \4.)Rajsthan \n5.)Telngana \n6.)Hariyana \nYour Choice :  ").strip().title()
      if state == "1" :
       
        finder.state_gujrat()
      elif state == "2":
        
        finder.state_maharastra()

      elif state == "3" :
        
        finder.state_tamil_nadu()

      elif state == "4" :
         
          finder.state_rajasthan()

      elif state == "5" :
       
       finder.state_telngana()

      elif state == "6" :
        print("Ok lets Find Best Eye Hospital in Haryana ✅")
        finder.state_haryana()
      break

  except Exception as e :
    print("Please Enter The Valid Detail ✅")



def find_best_hospital_near_you() :
  print("Ok lets Find Best Hospital Near You With Accurate Reasult ✔")
  try:
   while True :
     name = input("May i Have Your Name : ").strip().title()
     if name :
       print(f"Thank You {name} For Providing Your Detail ✅")
    
       break 
     else :
       print("Please Enter Your Name To Continue Further ✔")
    
   while True :
     option = input("For Which Type OF illness  Hospital Your Are Looking For \n1.)Big Hospital \n2.)Small Clinic \nYour Choice : ").strip()
     if option == "1" :
       print("Ok Let Me Find You Best Nearest Big Hospital That Make Sense For Your ✅ ")

       # we will introduce the location like state city and than we will go for illenss 

       select = input("To Find Best illness Hospital For Yor i Nedd Your illenss What Do you Have \n1.)Cancer\n2.)Kideny\3.)Heart \4.)Neurologist \n5.)Orthopadic \n6.)Eye \nYour Choice : ").strip()
       if select == "1":
         caner_hospital()
         break

       elif select == "2" :
         kidney_hospital()
         break
       elif select == "3" :
         heart_hospital()
         break

       elif select == "4" :
         neurology_hospital()
         break

       elif select == "5" :
         orthopadic_hospital()
         break

       elif select == "6" :
         eye_hospital()
         break

       else :
         print("Please Select An Above Option ✅")
     elif option == "2" :
       print("Ok lets Find Best Clinic Near You ✔")
       # here we impliment logic as we uploaded logic in class and funtion for big hospital same to same but for small
       # clinic class,fucntion and paste hiere
       state_clinic_doctor()



     else :
       print("Select An Valid Option ✔")
  except Exception as e:
    print("Please Enter Valid Optin To Continue Further ✔")


      

      # and we will add 1000+hospital data like every city will have atlest 50 best hospital in each state 
      #1000 is minimun reqriment



# i am impilemtning this logic and all the data will be store into database like name ,illness ,time ,hospital name



def book_appointment() :
  print("Ok Here We Are In Book Appointment Section ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    name = input("Enter Your Name : ").strip().title()
    hospital_name = input("Enter Hospital Name Where You Want To Book Appointment : ").strip().title()
    cursor.execute("SELECT * FROM hospital_doctors WHERE hospital_name = ?",(hospital_name,))
    rows = cursor.fetchall()
    if rows :
      print(f"Here is The Doctors List Of {hospital_name} ✔\n")
      for row in rows :
        name = (row["name"])
        specialization = (row["specialization"])
        print(f"Name: {name}, Specialization: {specialization}")
      doctor_name = input("Enter Doctor Name With Whom You Want To Book Appointment : ").strip().title()
      cursor.execute("SELECT * FROM hospital_doctors WHERE name = ? AND hospital_name = ?",(doctor_name,hospital_name))
      row = cursor.fetchone()
      if row :
        print(f"Ok Doctor {doctor_name} is Available in {hospital_name} ✔")
        appointment_date = input("Enter Appointment Date (DD-MM-YYYY) : ").strip()
        appointment_time = input("Enter Appointment Time (HH:MM AM/PM) : ").strip().upper()
        detail = {
          "name" : name,
          "hospital_name" : hospital_name,
          "doctor_name" : doctor_name,
          "appointment_date" : appointment_date,
          "appointment_time" : appointment_time,
          "time" : current_time
        }
        cursor.execute("""INSERT INTO appointments (name,hospital_name,doctor_name,appointment_date,appointment_time,time)
                       VALUES (?,?,?,?,?,?)""",(detail["name"],
                                                  detail["hospital_name"],
                                                  detail["doctor_name"],
                                                  detail["appointment_date"],
                                                  detail["appointment_time"],
                                                  detail["time"]
                                                  ))
        conn.commit()
        print(f"Appointment Booked Successfully With Dr.{doctor_name} On {appointment_date} At {appointment_time} ✔")
      else :
        print(f"Dr.{doctor_name} is Not Available in {hospital_name} ✔")
    else :
      print("No Doctors Data Found For This Hospital ✔")
  except Exception as e :
    print("The Occured Error is ",e)


def check_appointments() :
  print("Ok Here We Are In Check Appointments Section ✔")
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  try :
    name = input("Enter Your Name : ").strip().title()
    cursor.execute("SELECT * FROM appointments WHERE name = ?",(name,))
    rows = cursor.fetchall()
    if rows :
      print(f"Here is The Appointments List Of {name} ✔\n")
      for row in rows :
        doctor_name = (row["doctor_name"])
        appointment_date = (row["appointment_date"])
        appointment_time = (row["appointment_time"])
        print(f"Doctor Name: {doctor_name}, Appointment Date: {appointment_date}, Appointment Time: {appointment_time}")
    else :
      print("No Appointments Data Found ✔")
  except Exception as e :
    print("The Occured Error is ",e)





def doctor_panel() :
 print("Ok Here is Your Doctor Section ✔")
 print("1. View Profile")
 print("2. Update Profile")
 print("3. Logout")
 print("4. Add Doctor")
 print("5. View Patients")
 print("6. Add Patients")
 print("7. Check Appointments")

 choice = input("Enter Your Choice : ")
 if choice == "1" :
   doctor_view_profile()
 elif choice == "2" :
   doctor_update_profile()
 elif choice == "3" :
   doctor_logout()
 elif choice == "4" :
  add_doctor()
 elif choice == "5" :
   view_patients()
 elif choice == "6" :
  add_patients()
 elif choice == "7" :
  check_appointments()
 else :

   print("Invalid Choice ✔")

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
     cursor.execute("SELECT * FROM doctors WHERE name = ?",(name,))
     row = cursor.fetchone()
     if row :
       print("User Alrady Exist With This User Name.please Try With Diffent User Name")
     else :
       print("Ok User Name is Valid ")
       break
     while True :
      m_number = input("Enter Your 10 Digit Mobile Number For Comunication & Message : +91 ").strip().title()
    # here we ahve to put logic that if someone will register via here we will check the username in db 
    # before give the access if the same user name exist we will say no you can not regirster with this name
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



master = state_clinic_doctor()

welcome = input("Welcome To X Hospital : ")
option = input("Enter State : \n1.)Gujrat \n2.)Maharastra \n3.)Telngana \n4.)Rajshthan \n5.)Tamilnadu \n6.)Haryana \nYour Choice : ").strip()
if option == "1" :
  master.state_gujrat()
elif option == "2" :
  master.state_maharastra()
elif option == "3" :
  master.state_telngana()
elif option == "4":
  master.state_rajshtan()
elif option == "5":
  master.state_tamilnadu()
elif option == "6" :
  master.state_haryana()
else :
  print("Please Select Valid Option ✅")
