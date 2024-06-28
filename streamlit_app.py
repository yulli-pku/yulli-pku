import streamlit as st 
import pandas as pd 
import numpy as np
import requests
from st_aggrid import AgGrid

house=pd.read_csv("https://raw.githubusercontent.com/yulli-pku/yulli-pku/main/house_clean.csv")

def main() : 

  with st.form("Inputvar"):
    st.header('Input Variable Prediktif')
    icol1,icol2,icol3=st.columns(3)
    
    with icol1:
      idata1=st.text_input("input nilai data1")
    with icol2:
      idata2=st.text_input("input nilai data2")
    with icol3:
      idata3=st.text_input("input nilai data3")
      
    klikresult = st.form_submit_button('Cek Result')
    if klikresult :
      st.success(idata2)
    if st.success(idata2)='tidak sakit':
      st.balloons()
      st.snow()
        
  
   

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

#sidebar 
  sidebar_header=st.sidebar.subheader('Sidebar menu')
  nm=st.sidebar.selectbox("Pilih data", ["PT meong", "PT siapa sih", "PT selalu sukses"])
  st.sidebar.write("nama WP:",nm)
  sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
  sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])

    
  #columns :
  col1, col2, col3 = st.columns([1,1,1])

  with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    #atau dengan assignment 
    #image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")

  with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

  with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    #expander 
    #dengan with atau dengan assignment 
  expander = st.expander("Klik Untuk Detail ")
  expander.write('Anda Telah Membuka Detail')
  
  with st.form("Data Diri"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

  # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
      st.write("slider", slider_val, "checkbox", checkbox_val)
  
  st.write("Outside the form")

#tab
  tab1,tab2=st.tabs(["Tab 1","Tab 2"])
  tab1.write("this is tab 1")
  tab2.write("this is tab 2")

  with tab1:
    radio1=st.radio('Select one',[x for x in range(1,4)])
    st.write('Anda Memilih',radio1)
    
  with tab2:
    radio2=st.radio('Select one',['A','B'])
    st.write('Anda Memilih',radio2)

  st.balloons()
  st.snow()
  st.toast("Warming up...")
  st.error("Error message")
  st.warning("Warning message")
  st.info("Info message")
  st.success("Success message")
  st.line_chart(np.random.randn(30, 3))
  
  with st.chat_message("user"):
    st.write("Hello 👋")
    # Display a chat input widget at the bottom of the app.
    #st.chat_input("Say something")
    # Display a chat input widget inline.
    msg=st.chat_input("Say something")
    st.write(msg)

if __name__ == '__main__' : 
  main()

