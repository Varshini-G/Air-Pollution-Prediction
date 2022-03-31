# -*- coding: utf-8 -*-



import numpy as np
import pandas as pd
import sklearn as sk
import pickle
import streamlit as st




pickle_in = open("Random_forest_regressor.pkl","rb")
random_forest_regressor=pickle.load(pickle_in)


def welcome():
    return " welcome all"



def predict_AQI(Average_Temperature,Maximum_Temperature,Minimum_Temperature,Atm_pressure_at_sea_level,Average_wind_speed):
    
    
    prediction=random_forest_regressor.predict([[ Average_Temperature,Maximum_Temperature,Minimum_Temperature, Atm_pressure_at_sea_level,Average_wind_speed]])
    print(prediction)
    return prediction


def main():
    st.title("AQI prediction")
    html_temp = """
    <div style="background-color:green;padding:20px">
    <h2 style="color:white;text-align:center;">AQI prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Average_Temperature= st.text_input("Average_Temperature ",placeholder='Average_temp')
    Maximum_Temperature = st.text_input("Maximum_Temperature ",placeholder='Max_temp')
    Minimum_Temperature = st.text_input("Minimum_Temperature ",placeholder='Min_temp')
    Atm_pressure_at_sea_level = st.text_input("Atm_pressure_at_sea_level ",placeholder='Atm_pressure')
    Average_wind_speed = st.text_input("Average_wind_speed ",placeholder='Average_wind')
    result=""
    if st.button("Predict"):
        result=predict_AQI(Average_Temperature,Maximum_Temperature,Minimum_Temperature,Atm_pressure_at_sea_level,Average_wind_speed)
    st.success('The output is {}'.format(result))
   

if __name__=='__main__':
    main()
