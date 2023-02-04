import streamlit as st

def login():
    def read_users():
        users = []
        with open("student_login_data.txt") as f:
            for line in f:
                username, password = line.strip().split(",")
                users.append((username, password))
        return users
    
    
    users = read_users()
    
    def verify_user(username, password):
        return (username, password) in users
    
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if verify_user(username, password):
            st.success("Logged in")
        else:
            st.error("Incorrect username or password")