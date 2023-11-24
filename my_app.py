# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image# to deal with images (PIL: Python imaging library)

st.title("AutoScout Price Prediction Project by Using Machin Learning")
 


st.markdown('  Please Add Your Data Correctly To Predict Your Car Price  ')

# read the model we create
import pickle
filename = "my_model" 
model=pickle.load(open(filename, "rb"))




#take input from user 
type=st.selectbox("Please Select Your Veichle Type:", ["Used", "Pre-registered", "Demonstration","Employee's car"])

power_kW=st.number_input("Please Enter Your Veichle Power In KM:",min_value=0, max_value=500)


make_model=st.text_input("Please Enter Your Veichle Model: ")

# handling error from users
if make_model.isdigit() :
   st.error("Please Enter Name of Your Veichle Model ")
   
engine_size=st.number_input("Please Enter Your Engine Size:",min_value=1)





mileage=st.number_input("Please Enter mileage:",min_value=0)



age = st.slider("Please Enter Veichle Age:", min_value=0, max_value=80)



# Create a dataframe using feature inputs


my_dict = {"type":type,
           "power_kW":power_kW,
           "make_model":make_model,
           "engine_size":engine_size,
           "mileage":mileage,
           "age":age}

df = pd.DataFrame.from_dict([my_dict])

    
cbox= st.checkbox("Press The Button To See Your Data ")
if cbox :
    st.table(df)
    

# we add the input of the user to a model to predicted
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])
    
    
x= st.sidebar.button("AutoScout Price In 2023") 

if  x:
   img = Image.open("Infographic_AutoScout24_prices_Q1-2023_ENG_v2.jpg")
   st.image(img, caption="Price on Veichle in 2023", width=700)

st.sidebar.button("AutoScout Price Prediction") 



