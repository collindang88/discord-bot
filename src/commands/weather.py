from ..utils.c_log import log
import requests

@log('getting weather')
async def weather(ctx, *city):
    city = ' '.join(city) or 'Seattle'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': '92c4c4a2500128b450532048b03d6f53',
        'units': 'imperial'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        response = requests.get(url, params=params)
        data = response.json()

        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        humidity = data['main']['humidity']

        await ctx.send(f'The current weather in {params["q"]} is {weather}.')
        await ctx.send(f'The temperature is {temp:.2f} °F.')
        await ctx.send(f'The humidity is {humidity}%.')
    else:
        await ctx.send('Enter a valid location.')