import streamlit as st
import pandas as pd

st.title("Weather Forecast for the Next Days")
place = st.text_input("For which place would you like to know the weather?",
                      placeholder="Enter place name here")
days = st.slider("Number of Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days you'd like to know the weather forecast for.")

option = st.selectbox("Select type of data to view", ("Temperature", "Atmospheric Conditions"))

if place:
    if days == 1:
        st.subheader(f"{option} for {place} tomorrow")
    else:
        st.subheader(f"{option} for {place} for the next {days} days")
else:
    st.subheader("")

