import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.naive_bayes import GaussianNB

model = pickle.load(open('ramadhanpratamaputra_UTS.pkl', 'rb'))
st.title('Prediksi Terkena Diabetes')


Pregnancies = st.text_input('Kehamilan')
Glucose = st.text_input('Kadar Glukosa Dalam Darah')
BloodPressure = st.text_input('Ukuran Tekanan Darah')
SkinThickness = st.text_input('Ketebalan Kulit')
Insulin = st.text_input('Kadar Insulin Dalam Darah')
BMI = st.text_input('Indeks Masa Tubuh')
DiabetesPedigreeFunction = st.text_input('Presentase Diabetes')
Age = st.text_input('Inputkan Usia')

diabet_prediction = ''

if st.button('Prediksi Ibu Hamil Terkena Diabetes  adalah'):
    diabet_prediction = model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age,]])
st.success(diabet_prediction)
