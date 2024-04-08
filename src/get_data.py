import os
import requests


def get_space_weather(url="https://celestrak.org/SpaceData/SW-Last5Years.txt"):
    space_weather_filename = "/GMAT/R2022a/data/atmosphere/earth/SpaceWeather-v1.2.txt"

    response = requests.get(url)

    with open(space_weather_filename, "wb") as f:
        f.write(response.content)
