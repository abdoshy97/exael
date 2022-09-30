import streamlit as st
import pandas as pd
import openpyxl


st.set_page_config(page_title='Abdoshy App')
st.title('Excal Abd 📊')
st.subheader('this is test text')
u_file=st.file_uploader('Choose a XLSX file',type='xlsx')
if u_file:
    st.markdown('---')
    df=pd.read_excel(u_file,engine='openpyxl')
    st.dataframe(df)