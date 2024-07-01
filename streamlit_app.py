import pickle
import streamlit as st

model = pickle.load(open('knn_mode.pkl', 'rb'))

st.title('Cek Air Quality')

AQI= st.number_input('Input AQI')
PM10= st.number_input('Input PM10')
PM2_5= st.number_input('Input PM2_5')	
NO2= st.number_input('Input NO2')
SO2= st.number_input('Input SO2')	
O3= st.number_input('Input O3')
Temperature= st.number_input('Input Temperature')
Humidity= st.number_input('Input Humidity')	
WindSpeed= st.number_input('Input WindSpeed')
RespiratoryCases= st.number_input('Input RespiratoryCases')
CardiovascularCases	= st.number_input('Input CardiovascularCases')
HospitalAdmissions= st.number_input('Input HospitalAdmissions')

predict = ''

if st.button('Cek Air Quality'):
    predict = model.predict(
        [[AQI,PM10,PM2_5,NO2,SO2,O3,Temperature,Humidity,WindSpeed,RespiratoryCases,CardiovascularCases,HospitalAdmissions]]
    )
    st.write ('Cek Air Quality : ', predict)
