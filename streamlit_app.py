import streamlit as st 
import pandas as pd 
import requests
from st_aggrid import AgGrid

house=pd.read_csv("https://raw.githubusercontent.com/yulli-pku/yulli-pku/main/house_clean.csv")

def main() : 
  st.write('Minimal Example')

  st.header('Halaman Streamlit Yulli')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')
  st.write('Contoh dataframe')
  
  st.dataframe(house)
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  AgGrid(house)
  st.table([x for x in range(1,5)])
  
  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
    st.write('Anda Setuju')
    
  radio_button= st.radio('Choose below',[x for x in range(1,4)])
  st.write('Anda Memilih',radio_button)
    
  #slider 
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)
    
  #Input (Typing)
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))

if __name__ == '__main__' : 
  main()

