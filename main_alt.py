import streamlit as st
import plotly.express as px
from countries import better_country_converter, state_converter, CC
from forecast_backend import get_data, format_dates, get_data_specific


st.title("Generate a Custom Weather Forecast")
place = st.text_input("For which place would you like to know the weather?",
                      placeholder="Enter place name here", key="entered_place").casefold()

if place:
    capitalized_keys = [key.title() for key in better_country_converter.keys()]
    country = st.selectbox(options=capitalized_keys, label="Please select which country this place is in."
                                                           "  \n:violet[It's okay to leave this blank!]",
                           key="country_pick")
    st.write(f"The current country is {country}")
    state = st.selectbox(options=state_converter.keys(),label="If this place is in the U.S., please select which state it is in. "
                                                              ":pink[:violet[It's okay to leave this blank!]]",
                           key="state_pick")
    st.write(f"The current state is {state}")

days = st.slider("Number of Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days you'd like to know the weather forecast for.", key="days_pick")

forecast_type = st.selectbox(options=("Temperature", "Atmospheric Conditions"),
                             label=":green[Select type of data to view]", key="forecast_pick").casefold()


if place:
    rawdata, data = get_data_specific(place, country, state, days)
    st.write(rawdata)
    st.write(rawdata["city"]["country"])
    country_called_upon = rawdata["city"]["country"]
    country_called_upon = CC[country_called_upon].title()
    if days == 1:
        st.subheader(f"{forecast_type.title()} for {place.title()} in {country_called_upon} tomorrow")
    else:
        st.subheader(f"{forecast_type.title()} for {place.title()} in {country_called_upon} for the next {days} days")
else:
    st.subheader("")

if place:
    if forecast_type == "temperature":
        temperatures = [DAY["main"]["temp"] for DAY in data]
        dates = [DAY["dt_txt"] for DAY in data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date",
                                              "y": "Temperatures (F)"})  # Notice labels accepts a DICTIONARY as its input.
        st.plotly_chart(figure)

    if forecast_type == "atmospheric conditions":
        images = {"Clear": "https://drive.google.com/uc?id=1GslstA5FMGQdj9r2iiqp4yZ9Eoaoolab",
                  "Clouds": "https://drive.google.com/uc?id=1O5PO5jYuIKUfVhNU1Oup_8lJWFPENGPe",
                  "Rain": "https://drive.google.com/uc?id=1LHBE5RVm47jXY_rXGjWQPLWtuXjIhlpW",
                  "Snow": "https://drive.google.com/uc?id=1cPFMhm_m3yRTHGsNxTuajfCEPJvowbre"}

        skies_description = [DAY["weather"][0]["description"].title() for DAY in data]
        skies_conditions = [DAY["weather"][0]["main"] for DAY in data]
        skies_description = [DAY["weather"][0]["description"].title() for DAY in data]
        dates = [DAY["dt_txt"] for DAY in data]
        new_dates = format_dates(dates)
        captions = [f"{date}, {desc}" for date, desc in zip(new_dates, skies_description)]
        image_paths = [images[condition] for condition in skies_conditions]
        st.image(image_paths, caption=captions, width=120)



# old code; uncomment to run it.
# def get_data(days):
#     dates = ["2022-25-10", "2022-26-10", "2022-31-10"]
#     temperatures = ["20", "6", "23"]
#     # Make the graph interactive
#     temperatures = [days * i for i in temperatures]
#     return dates, temperatures
#
# d,t = get_data(days)
#


st.write()
st.write(st.session_state)