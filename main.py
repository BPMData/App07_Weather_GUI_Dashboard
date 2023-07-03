import streamlit as st
import pandas as pd
import plotly.express as px
from forecast_backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("For which place would you like to know the weather?",
                      placeholder="Enter place name here", key="entered_place").casefold()

days = st.slider("Number of Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days you'd like to know the weather forecast for.")

forecast_type = st.selectbox(options=("Temperature", "Atmospheric Conditions"),
                             label=":green[Select type of data to view]", key="forecast_type").casefold()

if place:
    if days == 1:
        st.subheader(f"{forecast_type} for {place.title()} tomorrow")
    else:
        st.subheader(f"{forecast_type} for {place.title()} for the next {days} days")
else:
    st.subheader("")

data = get_data(place, days, forecast_type)

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-31-10"]
    temperatures = ["20", "6", "23"]
    # Make the graph interactive
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d,t = get_data(days)

figure = px.scatter(x=d, y=t, labels={"x": "Date", "y": "Temperatures (F)"})  #Notice labels accepts a DICTIONARY as its input.

st.plotly_chart(figure)

st.write(st.session_state)