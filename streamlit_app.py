!pip install streamlit-aggrid
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
  st.table([x for x in range(1,5)])
if __name__ == '__main__' : 
  main()

