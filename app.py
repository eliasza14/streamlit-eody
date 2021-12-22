import pandas as pd

from datetime import date,timedelta, datetime
import streamlit as st
import base64
import io
import calendar


showButton=0
#Replace the name of file 
uploaded_file = st.file_uploader("Load your Dataset")
if uploaded_file is not None:
     df = pd.read_excel(uploaded_file , dtype={'Έναρξη':str, 'Λήξη':str, 'Περιφέρεια':str, 'ΚΟΜΥ':str, 'Κατηγορία':str, 'Χρήστης':str,
       'Προσωπικό':str, 'Άδεια':str, 'Σχόλια':str, 'Χρήστης τροποποίησης':str,
       'Ημέρα τροποποίησης':str, 'Ώρες':str, 'Ώρες*':str   })
     st.dataframe(df)
     df[['datestart', 'time']] = df['Έναρξη'].str.split(' ', expand=True)
     df[['dateend', 'timeend']]= df['Λήξη'].str.split(' ', expand=True)
     #Find Duplicates and add boolean column on dataset
     duplicates=df.duplicated(subset=['Χρήστης','datestart'],keep=False)
     df['Boolean Duplicate']=duplicates
     st.dataframe(df.loc[325:330])
     showButton=1
     


if (showButton!=0):
    towrite = io.BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode() 
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="myfilename.xlsx">Download excel file</a>'
    st.markdown(linko, unsafe_allow_html=True)






