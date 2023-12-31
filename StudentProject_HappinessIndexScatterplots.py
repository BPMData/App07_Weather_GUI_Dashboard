import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("C:\PythonProjects\App07_Weather_GUI_Dashboard\data\happy.csv")

st.title("Correlations Between Happiness and Various National Statistics")

xselect = st.selectbox(label=":green[Select the data for the X-axis]", key="firstbox",
             options=("GDP", "Happiness", "Generosity"), index=0)
xselect2 = xselect.casefold()



yselect = st.selectbox(label=":orange[Select the data for the Y-axis]", key="secondbox",
                     options=("GDP", "Happiness", "Generosity"), index=1)
yselect2 = yselect.casefold()

st.write(yselect)

xaxis = df[f"{xselect2}"]
yaxis = df[f"{yselect2}"]


figure1 = px.scatter(x=xaxis, y=yaxis, labels={"x": f"{xselect}",
                                              "y": f"{yselect}"},
                    title=f"{yselect} plotted against {xselect} for 145 Selected Countries",
                    color=df["country"])  #Notice labels accepts a DICTIONARY as its input.
# This works but is kinda hacky.

# Below is better:
figure2 = px.scatter(x=xaxis, y=yaxis, labels={"x": f"{xselect}",
                                              "y": f"{yselect}"},
                    title=f"{yselect} plotted against {xselect} for 145 Selected Countries",
                    hover_name=df["country"])

# There are a LOT of options for hover label modifications in Plotly. Check them out here:
# https://plotly.com/python/hover-text-and-formatting/
# Here's another interesting streamlit article:
# https://andymcdonaldgeo.medium.com/uploading-and-reading-files-with-streamlit-92885ac3a1b6

figure2.update_layout(
    title={
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24} # Change the size of the title
    },
    yaxis_title={
        'font': {'color': 'orange'} # Change the color of the y-axis label
    },
    xaxis_title={
        'font': {'color': 'green'} # Change the color of the x-axis label
    }
)

st.plotly_chart(figure2)
