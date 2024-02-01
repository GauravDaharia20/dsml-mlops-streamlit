import streamlit as st
import pandas as pd
import pickle

st.title("Car Price Prediction App")

# Four inputs from the user
# Fuel type, Transmission type, engine power, number of seats

col1, col2 = st.columns(2)

with col1:
    fuel_type = st.radio("Fuel", options=["Petrol", "Diesel", "CNG", "LPG", "Electric"])

with col2:
    transmission_type = st.selectbox("Transmission Type", options=["Manual", "Automatic"])

col3, col4 = st.columns(2)

with col3:
    engine_power = st.slider("Engine Power", 500, 5000, step=100)

with col4:
    seats = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9, 10])
years = st.slider("Years", 2013, 2021, step=1)


model = pickle.load(open("car_pred", "rb"))
encode_dict = {
    "fuel_type": {
        "Diesel": 1,
        "Petrol": 2,
        "CNG": 3,
        "LPG": 4,
        "Electric": 5
    },
    "transmission_type": {
        "Manual": 1,
        "Automatic": 2
    }
}

def model_pred(fuel_type, transmission_type, engine_power, seats, years):
    transmission_type = encode_dict['transmission_type'][transmission_type]
    fuel_type = encode_dict['fuel_type'][fuel_type]

    data = [[years, 1, 40000, fuel_type, transmission_type, 18.0, engine_power, 85, seats]]

    return round(model.predict(data)[0], 2)

if st.button("Predict"):
    st.write(model_pred(fuel_type, transmission_type, engine_power, seats, years))
else:
    st.write("Click on predict")
