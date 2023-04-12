import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import requests
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = 218594256665706497
CHANNEL_ID = 218594256665706497
COLLIN_ID = 414133543803813915
DENNIS_ID = 191663954806833153
dennis_count = 0
NIKHIL_ID = 288830770863144960

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

async def say_msg():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    while not bot.is_closed():
        await channel.send("why you living in the past cuh")
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your bot!')

@bot.command()
async def sing(ctx):
    await ctx.send('lalalalala')

@bot.command()
async def gpt(ctx, *input):
    if ctx.author.id == DENNIS_ID:
        dennis_count += 1
    if dennis_count >= 10:
        return

    prompt = ' '.join(input)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        await ctx.send(response.choices[0].message.content.strip())
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
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


@bot.event
async def on_message(message):
    # if message.author.id == DENNIS_ID:
    #     channel = message.channel
    #     await channel.send('why you stuck in the past cuh')
    if 'hi bot' == message.content.lower():
        channel = message.channel
        await channel.send(f'hi {message.author}')
    await bot.process_commands(message)

async def main():
    # asyncio.create_task(say_msg())
    await bot.start(TOKEN)

asyncio.run(main())
