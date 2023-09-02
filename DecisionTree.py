import streamlit as st
import pandas as pd
import pickle
from io import BytesIO
import requests

st.title('ML Prediction App')
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])
response = requests.get("https://github.com/Norris0333/Simbolo_Structured_Data_Project/blob/raw/main/train_model.pkl")

if response.status_code == 200:
    model_content = response.content
    # Load the trained model using pickle
    model = pickle.loads(model_content)
else:
    st.error('Failed to load the model. Please check the URL.')

if uploaded_file is not None:
    # Read the uploaded .csv file
    data = pd.read_csv(uploaded_file)
    file_X = data.iloc[:, 0:-1].values
    file_Y = data.iloc[:, -1].values
    predictions = model.predict(file_X)
    # Display the predictions
    st.write('Predictions:')
    st.write(predictions)
    st.write('True values:')
    st.write(file_Y)
