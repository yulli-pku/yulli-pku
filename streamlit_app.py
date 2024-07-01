import pickle
import streamlit as st

model = pickle.load(open('knn_model.pkl', 'rb'))

st.title('Cek Air Quality')

with st.form("Inputvar"):
    st.sidebar.header('Input Variable Prediktif Air')
    AQI= st.sidebar.number_input('Input AQI')
    PM10= st.sidebar.number_input('Input PM10')
    PM2_5= st.sidebar.number_input('Input PM2_5')	
    NO2= st.sidebar.number_input('Input NO2')
    SO2= st.sidebar.number_input('Input SO2')	
    O3= st.sidebar.number_input('Input O3')
    Temperature= st.sidebar.number_input('Input Temperature')
    Humidity= st.sidebar.number_input('Input Humidity')	
    WindSpeed= st.sidebar.number_input('Input WindSpeed')
    RespiratoryCases= st.sidebar.number_input('Input RespiratoryCases')
    CardiovascularCases	= st.sidebar.number_input('Input CardiovascularCases')
    HospitalAdmissions= st.sidebar.number_input('Input HospitalAdmissions')
    HealthImpactClass= st.sidebar.number_input('Input HealthImpactClass')

predict = ''

if st.button('Cek Air Quality'):
    predict = model.predict(
        [[AQI,PM10,PM2_5,NO2,SO2,O3,Temperature,Humidity,WindSpeed,RespiratoryCases,CardiovascularCases,HospitalAdmissions,HealthImpactClass]]
    )
    st.write ('Cek Air Quality : ', predict)
