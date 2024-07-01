import pickle
import streamlit as st

model = pickle.load(open('knn_model.pkl', 'rb'))
st.title('Cek Air Quality')
st.image("kotaair.png")

with st.form("Inputvar"):
    st.sidebar.header('Input Variable Prediktif Air')   
    
    AQI= st.sidebar.slider('Input AQI',0.00,10.00)
    st.write('AQI : ',AQI)
    PM10= st.sidebar.slider('Input PM10',0.00,10.00)
    st.write('PM10 : ',PM10)
    PM2_5= st.sidebar.slider('Input PM2_5',0.00,10.00)	
    st.write('PM2_5 : ',PM2_5)
    NO2= st.sidebar.slider('Input NO2',0.00,10.00)
    st.write('NO2 : ',NO2)
    SO2= st.sidebar.slider('Input SO2',0.00,10.00)	
    st.write('SO2 : ',SO2)
    O3= st.sidebar.slider('Input O3',0.00,10.00)
    st.write('O3 : ',O3)
    Temperature= st.sidebar.slider('Input Temperature',0.00,10.00)
    st.write('Temperature : ',Temperature)
    Humidity= st.sidebar.slider('Input Humidity',0.00,10.00)
    st.write('Humidity : ',Humidity)	
    WindSpeed= st.sidebar.slider('Input WindSpeed',0.00,10.00)
    st.write('WindSpeed : ',WindSpeed)
    RespiratoryCases= st.sidebar.slider('Input RespiratoryCases',0,100)
    st.write('RespiratoryCases : ',RespiratoryCases)
    CardiovascularCases	= st.sidebar.slider('Input CardiovascularCases',0,100)
    st.write('CardiovascularCases : ',CardiovascularCases)
    HospitalAdmissions= st.sidebar.slider('Input HospitalAdmissions',0,100)
    st.write('HospitalAdmissions : ',HospitalAdmissions)
    HealthImpactClass= st.sidebar.slider('Input HealthImpactClass',0,100)
    st.write('HealthImpactClass : ',HealthImpactClass)

predict = ''

if st.button('Cek Air Quality'):
    predict = model.predict(
        [[AQI,PM10,PM2_5,NO2,SO2,O3,Temperature,Humidity,WindSpeed,RespiratoryCases,CardiovascularCases,HospitalAdmissions,HealthImpactClass]]
    )
    st.write ('Kondisi Udara diprediksi : ', predict)
