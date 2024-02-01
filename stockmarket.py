import streamlit as st 
import pandas as pd 
import yfinance as yf
import numpy as np

st.title('Stock Market App')
st.write('This is my first stock market application using streamlit and I will conquire the world !!!')

# Taking user input
user_stock_input = st.text_input("Enter Stock Ticker Symbol","AAPL")

starting_date = st.date_input("Enter the starting date",value=pd.to_datetime("2022-05-01"))
ending_date = st.date_input("Enter the ending date",value=pd.to_datetime("today"))

stock_symbol = user_stock_input
df = yf.Ticker(stock_symbol)

hist = df.history(start=starting_date,end=ending_date)
st.dataframe(hist)
title = "Apple"
if(user_stock_input=="MSFT"):
    title = "MicroSoft Data"

st.title(title)
# for giving output in columns
col1 , col2 = st.columns(2)
with col1:
    st.write("Volume Trend")
    st.line_chart(data=hist.Volume)
with col2:
    st.write("Price Trend")
    st.line_chart(data=hist.Close)
