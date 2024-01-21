import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.naive_bayes import GaussianNB
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px

with st.sidebar:
    selected = option_menu('Aplikasi Klasifikasi Diabetes', ['Klasifikasi Diabetes', 'Keterangan Label Data Set'],
                           icons=['house', 'gear'], menu_icon="cast", default_index=0)

if (selected == 'Klasifikasi Diabetes'):
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


if (selected == 'Keterangan Label Data Set'):
    st.title('Keterangan Diabetes')
    img = Image.open('diabetes.jpg')
    st.image(img, use_column_width=False)
    st.write("""
         # 
1. Pregnancies: Untuk menyatakan Jumlah kehamilan

2. Glucose : Untuk menyatakan kadar Glukosa dalam darah

3 BloodPressure Untuk menyatakan pengukuran tekanan darah

4. SkinThickness: Untuk menyatakan ketebalan kulit

5. Insulin: Untuk menyatakan kadar Insulin dalam darah

6. BMI: Untuk menyatakan indeks massa tubuh

7. DiabetesPedigreeFunction : Untuk menyatakan persentase Diabetes

8. Age: Untuk menyatakan usia.

9. Outcome :Untuk menyatakan hasil akhir 1 adalah Ya dan 0 adalah Tidak
         """
             )
