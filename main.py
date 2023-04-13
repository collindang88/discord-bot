import discord
from discord.ext import commands
import asyncio
import openai

from src.commands.gpt import gpt
from src.commands.weather import weather
from src.events.events import on_ready, on_message
from src.utils.constants import DISCORD_TOKEN, OPENAI_API_KEY

async def main():
    openai.api_key = OPENAI_API_KEY

    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    bot.add_command(commands.Command(gpt, name="gpt"))
    bot.add_command(commands.Command(weather, name="weather"))
    bot.on_ready = lambda: on_ready(bot)
    bot.on_message = lambda message: on_message(bot, message)
    
    await bot.start(DISCORD_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
