import streamlit as st
import pandas as pd
from PIL import Image
import hashlib
import sqlite3
import os
import numpy as np
import cv2
from qrcode_f import make_qr
import time

# Current Path
current_path = os.path.dirname(__file__)

# Images
image_hsd_logo = Image.open(f'{current_path[:-14]}\\images\\hsd_logo.png')


# Change password to hash for security

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management
conn = sqlite3.connect('students.db')
c = conn.cursor()


# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS login_data(username TEXT, password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO login_data(username, password) VALUES (?,?)', (username, password))
    make_qr(username, username)
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM login_data WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM login_data')
    data = c.fetchall()
    return data


def main():
    """HSD Digital ID"""

    st.image(image_hsd_logo)
    st.title("Digital ID")

    menu = ["Home", "Login", "SignUp", "Scan"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Login"):
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))

                task = st.selectbox("What do you want?", ["QR-Code", "Matriculation certificate", "Overview"])
               
                if task == "Overview":
                    st.subheader("Personal Information".format(username))
                    
                    container_student_id = st.container()
                    container_student_id.write("Student ID: {}")
                    
                    container_firstname = st.container()
                    container_firstname.write("First Name: {}")
                    
                    container_lastname = st.container()
                    container_lastname.write("Last Name: {}")
                    
                    container_birthday = st.container()
                    container_birthday.write("Birthday: {}")
                    
                    container_course = st.container()
                    container_course.write("Course: {}") 

                elif task == "Matriculation certificate":
                    st.subheader("Matriculation certificate from {}".format(username))
               
                    container_matriculation = st.container()
                    container_matriculation.write("Download your Matriculation certificate here: {}")

                elif task == "QR-Code":
                    st.subheader("QR-Code from {}".format(username))
                    
                    container_qr_code = st.container()
                    container_qr_code.write("Here is your personal QR-Code:") 
                    
                    image_qr_code = Image.open(f'{current_path[:-14]}\\Datasets\\Qr_codes\\{username}.png')
                    st.image(image_qr_code)
                    
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
    

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_username, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
    
    elif choice == "Scan":
        
        if "imageCaptured" not in st.session_state.keys():
            st.session_state["imageCaptured"] = None
        col1, col2 = st.columns(2)
            
        with col1:
            captureQrCode = st.camera_input("Qr Code scanner", help= "drücke auf Take Photo, wenn der Qr Code gut sichtbar ist")
            
            if captureQrCode:
                st.session_state["imageCaptured"] = captureQrCode
                
        with col2:
            st.write("Die Nachricht des Qr codes")
            
            if st.session_state["imageCaptured"]:
                img = Image.open(st.session_state["imageCaptured"])
                openCvImage = np.array(img)
                 
                qrCodeDetector = cv2.QRCodeDetector()
                data = qrCodeDetector.detectAndDecode(openCvImage)
                st.write(data[0])
        
if __name__ == '__main__':
    main()
