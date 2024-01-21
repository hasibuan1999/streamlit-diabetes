import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.naive_bayes import GaussianNB
from streamlit_option_menu import option_menu
import plotly.express as px

st.title('Prediksi Terkena Diabetes')
model = pickle.load(open('ramadhanpratamaputra_UTS.pkl', 'rb'))

Pregnancies = st.text_input('Kehamilan')
Glucose = st.text_input('Kadar Glukosa Dalam Darah')
BloodPressure = st.text_input('Ukuran Tekanan Darah')
SkinThickness = st.text_input('Ketebalan Kulit')
Insulin = st.text_input('Kadar Insulin Dalam Darah')
BMI = st.text_input('Indeks Masa Tubuh')
DiabetesPedigreeFunction = st.text_input('Presentase Diabetes')
Age = st.text_input('Inputkan Usia')

diabet_prediction = ''

# membuat tombol predisksi
if st.button('Prediksi Ibu Hamil Terkena Diabetes  adalah'):
        diabet_prediction = model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age,]])
        if(diabet_prediction[0] == 1):
            diabet_prediction = 'Pasien Terkena Diabetes'
        else :
            diabet_prediction = "Pasien Tidak Terkena Diabetes"
        st.success(diabet_prediction)
