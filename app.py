import pandas as pd

from datetime import date,timedelta, datetime
import streamlit as st

import calendar

#Replace the name of file 
uploaded_file = st.file_uploader("Load your Dataset")
if uploaded_file is not None:
     df = pd.read_excel(uploaded_file , dtype={'Έναρξη':str, 'Λήξη':str, 'Περιφέρεια':str, 'ΚΟΜΥ':str, 'Κατηγορία':str, 'Χρήστης':str,
       'Προσωπικό':str, 'Άδεια':str, 'Σχόλια':str, 'Χρήστης τροποποίησης':str,
       'Ημέρα τροποποίησης':str, 'Ώρες':str, 'Ώρες*':str   })
     st.write(df)
     df[['datestart', 'time']] = df['Έναρξη'].str.split(' ', expand=True)
     df[['dateend', 'timeend']]= df['Λήξη'].str.split(' ', expand=True)
     #Find Duplicates and add boolean column on dataset
     duplicates=df.duplicated(subset=['Χρήστης','datestart'],keep=False)
     df['Boolean Duplicate']=duplicates
     st.write(df.loc[325:330])

     # Export to Excel File for Editing 
     datatoexcel = pd.ExcelWriter('C:\\Users\\admin\\Desktop\\fileduplicatedates-november-LAMPRIN2.xlsx')
    
     df.to_excel(datatoexcel) 

     datatoexcel.save()







