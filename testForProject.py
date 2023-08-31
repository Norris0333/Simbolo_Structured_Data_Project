# import streamlit as st
# import pandas as pd
# import os

# directory_path = '/ProjectCSV/Sampletrainingdata.csv'
# os.makedirs(directory_path)

# df = pd.read_csv(directory_path)


# st.table(df)




import streamlit as st
import pandas as pd
import openpyxl

e = RuntimeError('Only For Our xlsx file hehe.(!!!EXCLUSIVE!!!)')
st.exception(e)

st.title('XLSX File Viewer')

uploaded_file = st.file_uploader('Upload a xlsx file', type=['xlsx'])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    # Specify the x, y, and z columns for the bar chart
    x_column = st.selectbox('State_and_Region', df.columns)
    y_column = st.selectbox('Pred_Poverty_HC', df.columns)
#     z_column = st.selectbox(, df.columns)

    # Create a bar chart using the specified columns
    st.bar_chart(df[[x_column, y_column]])
