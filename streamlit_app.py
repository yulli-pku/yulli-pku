import pickle
import streamlit as st

model = pickle.load(open('knn_model.pkl', 'rb'))
st.title('Cek Air Quality')
st.image("kotaair.png")

with st.form("Inputvar"):
    st.sidebar.header('Input Variable Prediktif Air')
    AQI= st.sidebar.slider('Input AQI',0.00,10.00)
    PM10= st.sidebar.slider('Input PM10',0.00,10.00)
    PM2_5= st.sidebar.slider('Input PM2_5',0.00,10.00)	
    NO2= st.sidebar.slider('Input NO2',0.00,10.00)
    SO2= st.sidebar.slider('Input SO2',0.00,10.00)	
    O3= st.sidebar.slider('Input O3',0.00,10.00)
    Temperature= st.sidebar.slider('Input Temperature',0.00,10.00)
    Humidity= st.sidebar.slider('Input Humidity',,0.00,10.00)	
    WindSpeed= st.sidebar.slider('Input WindSpeed',,0.00,10.00)
    RespiratoryCases= st.sidebar.slider('Input RespiratoryCases',0,100)
    CardiovascularCases	= st.sidebar.slider('Input CardiovascularCases',0,100)
    HospitalAdmissions= st.sidebar.slider('Input HospitalAdmissions',0,100)
    HealthImpactClass= st.sidebar.slider('Input HealthImpactClass',0,100)

predict = ''

if st.button('Cek Air Quality'):
    predict = model.predict(
        [[AQI,PM10,PM2_5,NO2,SO2,O3,Temperature,Humidity,WindSpeed,RespiratoryCases,CardiovascularCases,HospitalAdmissions,HealthImpactClass]]
    )
    st.write ('Kondisi Udara diprediksi : ', predict)
