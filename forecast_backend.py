import streamlit as st
import requests
import pandas as pd

weather_key = st.secrets["WEATHER_API"]

city_name = ""

def get_data(place, days=None, forecast_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={weather_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values_needed = 8*days
    filtered_data = filtered_data[:nr_values_needed]
    if forecast_type == "temperature":
        filtered_data = [DAY["main"]["temp"] for DAY in filtered_data]
    if forecast_type== "atmospheric conditions":
        # His code:
        # filtered_data = [DAY["weather"][0]["main"] for DAY in filtered_data]
        # I prefer:
        filtered_data = [DAY["weather"][0]["description"].title() for DAY in filtered_data]
    return filtered_data

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


if __name__ == "__main__":
    testoutput = get_data(place="London", days=1, forecast_type="atmospheric conditions")
    print(testoutput)

    # dftemp = pd.DataFrame()
    # for day in testoutput["list"]:
    #     temp = day["main"]["temp"]
    #     dftemp = pd.concat([dftemp, pd.DataFrame({"Temperature": [temp]})], ignore_index=True)
    # print(dftemp)
