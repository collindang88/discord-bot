# Third Party
import requests

# First Party
from src.utils.c_log import log
from src.utils.constants import OPENWEATHERMAP_API_KEY


@log("getting weather")
async def weather(ctx, *city):
    city = " ".join(city) or "Seattle"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPENWEATHERMAP_API_KEY, "units": "imperial"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        response = requests.get(url, params=params)
        data = response.json()

        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        await ctx.send(f'The current weather in {params["q"]} is {weather}.')
        await ctx.send(f"The temperature is {temp:.2f} °F.")
        await ctx.send(f"The humidity is {humidity}%.")
    else:
        await ctx.send(response.text)
