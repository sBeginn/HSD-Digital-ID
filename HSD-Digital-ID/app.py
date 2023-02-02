import streamlit as st

with open("login_page.py", "r") as f:
    code = f.read()

exec(code)