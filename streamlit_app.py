import streamlit as st 

def main() : 
  st.write('Minimal Example')

  st.header('Halaman Streamlit Yulli')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')
  
if __name__ == '__main__' : 
  main()

