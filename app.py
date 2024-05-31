import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('D:/Internship-1/CodeClause/Task/Task-3 Heart_Disease/random-forest-model.pkl', 'rb'))

def heart_disease_prediction(input_data):
    data = np.asarray(input_data)
    data = data.reshape(1, -1)
    prediction = loaded_model.predict(data)

    if prediction == 1:
        return "Person is having Heart Disease!!❤️‍🩹😟🤕"
    else:
        return "Person is not having Heart Disease, Not to worry!!😇😊"

def main():

    st.title('Heart Disease Prediction App')

    st.sidebar.title('User Input Features')

    Age = st.sidebar.slider('Age', 20, 80, 50)
    Sex = st.sidebar.selectbox('Sex', ['Male', 'Female'])
    Chest_Pain = st.sidebar.selectbox('Chest Pain Type', ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'])
    Blood_Pressure = st.sidebar.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120)
    Cholesterol = st.sidebar.slider('Serum Cholesterol (mg/dl)', 100, 400, 200)
    Blood_Sugar = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])
    Resting_ECG = st.sidebar.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
    Max_HeartRate = st.sidebar.slider('Maximum Heart Rate Achieved', 60, 200, 150)
    Angina = st.sidebar.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    Oldpeak = st.sidebar.number_input('ST Depression Induced by Exercise Relative to Rest', 0.0, 5.0, 1.0, step=0.1)
    Slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    Vessel = st.sidebar.selectbox('Number of Major Vessels Colored by Fluoroscopy', [0, 1, 2, 3])
    Thalassemia = st.sidebar.selectbox('Thalassemia', ['Normal', 'Fixed defect', 'Reversible defect'])


    Sex = 1 if Sex == 'Male' else 0
    Chest_Pain = {'Typical angina': 0, 'Atypical angina': 1, 'Non-anginal pain': 2, 'Asymptomatic': 3}[Chest_Pain]
    Blood_Sugar = 1 if Blood_Sugar == 'True' else 0
    Resting_ECG = {'Normal': 0, 'ST-T wave abnormality': 1, 'Left ventricular hypertrophy': 2}[Resting_ECG]
    Angina = 1 if Angina == 'Yes' else 0
    Slope = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}[Slope]
    Thalassemia = {'Normal': 0, 'Fixed defect': 1, 'Reversible defect': 2}[Thalassemia]

    
    input_data = [Age, Sex, Chest_Pain, Blood_Pressure, Cholesterol, Blood_Sugar, Resting_ECG, Max_HeartRate, Angina, Oldpeak, Slope, Vessel, Thalassemia]

    diagnosis = ""

    if st.button('Predict'):
        diagnosis = heart_disease_prediction(input_data)

    st.success(diagnosis)

if __name__ == '__main__':
    main()

