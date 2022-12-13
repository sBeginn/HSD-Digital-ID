import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Help: https://www.datacamp.com/tutorial/streamlit

#Start Page Name,Bild + Authentication 
st.title("HSD-Digital-Card")
st.header("Hochschule Düsseldorf")
st.image("hsd.jpg")
# + Authentication

#Page 1 Home Info about Student
st.title("Student-Info")
st.markdown("Vor- und Nachname")
st.markdown("Geburtsdatum")
st.markdown("Adresse")
st.markdown("Immatrikuliert Ja/Nein")

#Page 2 Info Semester Grades
df= pd.DataFrame(
    np.random.randn(10, 2), #Hier sollen dann daten zu noten sein (5fächer)
    columns=['x', 'y'])
st.line_chart(df)

#Page 3 Immatrikulationsbescheinigung
st.title("Immatrikulationsbescheinigung")
st.image("Immatrikulationsbescheinigung.jpg")

#Page 4 QR-Code
st.title("QR-Code")
st.image("QR-Code.jpg")

#Create selection for Pages
@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Grades','Certificate','QR-Code' ]) #four pages

