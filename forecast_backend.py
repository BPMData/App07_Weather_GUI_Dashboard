import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from countries import better_country_converter, state_converter

weather_key = st.secrets["WEATHER_API"]

city_name = ""

def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={weather_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values_needed = 8*days
    filtered_data = filtered_data[:nr_values_needed]
    # Gonna move all these if statements into the frontend code:
    return filtered_data

    """if forecast_type == "temperature":
    if forecast_type == "temperature":
    data = [DAY["main"]["temp"] for DAY in data]
    if forecast_type== "atmospheric conditions":
        # His code:
        # filtered_data = [DAY["weather"][0]["main"] for DAY in filtered_data]
        # I prefer:
        filtered_data = [DAY["weather"][0]["description"].title() for DAY in filtered_data]
    
    """

"""
The actual APIs:

[DEPRECATED]
https://openweathermap.org/forecast5#geocoding
api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
api.openweathermap.org/data/2.5/forecast?q={city name},{country code}&appid={API key}
api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key} 
[DEPRECATED]

Current APIs:
https://openweathermap.org/forecast5

api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key} 
https://openweathermap.org/api/geocoding-api 
 
"""

# This was a lot more annoying to develop than I expected:

def format_dates(list):
    formatted_dates = []
    for date in list:
        dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        formatted_date = dt.strftime("%B %d - %I:%M %p")
        formatted_dates.append(formatted_date)
    return formatted_dates

if __name__ == "__main__":
    testoutput = get_data(place="London", days=1)
    print(testoutput)

    # dftemp = pd.DataFrame()
    # for day in testoutput["list"]:
    #     temp = day["main"]["temp"]
    #     dftemp = pd.concat([dftemp, pd.DataFrame({"Temperature": [temp]})], ignore_index=True)
    # print(dftemp)

def get_data_specific(place=None, country=None, state=None, days=None):
    country_code = None
    state_code = None
    if country is not None:
        country = country.upper()
        print(country)
        country_code = better_country_converter[country]
        print(country_code)
    if state is not None:
        state = state.title()
        print(state)
        state_code = state_converter[state]
        print(state_code)
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place},{state_code},{country_code}&appid={weather_key}&units=imperial"
    response = requests.get(url)
    rawdata = response.json()
    filtered_data = rawdata["list"]
    if days is not None:
        nr_values_needed = 8*int(days)
        filtered_data = filtered_data[:nr_values_needed]
    # Gonna move all these if statements into the frontend code:
    return rawdata, filtered_data

output = get_data_specific("London", state="Ohio", country="United States", days="3")

def get_data_properly(lat,lon,days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={weather_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values_needed = 8*days
    filtered_data = filtered_data[:nr_values_needed]
    return filtered_data

def get_geo(city=None, state=None, country=None):
    country_code = None
    state_code = None
    if state is not "":
        state = state.title()
        print(state)
        state_code = state_converter[state]
        print(state_code)
    else:
        state_code = ""
    if country is not "":
        country = country.upper()
        print(country)
        country_code = better_country_converter[country]
        print(country_code)
    else:
        country_code = ""
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&limit=1&appid={weather_key}"
    response = requests.get(url)
    rawdata = response.json()
    needed = (rawdata[0]["lat"], rawdata[0]["lon"])
    return rawdata, needed