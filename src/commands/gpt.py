# Third Party
import openai
import datetime as dt
from termcolor import cprint

# First Party
from src.utils.c_log import log

conversations = {}

async def send_response_chunks(ctx, message_chunks):
    for chunk in message_chunks:
        await ctx.send(chunk)

async def gpt(ctx):
    user_id = str(ctx.author.id)
    prompt = ctx.message.content[4:].strip()

    if user_id == '686643495062339611': # banning eli
        await ctx.send('you have been target banned from using this bot by collin')
        return

    if user_id not in conversations:
        conversations[user_id] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    conversations[user_id].append({"role": "user", "content": prompt})

    cprint(f"[{dt.datetime.now()}] User ID: {user_id}", "green")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview", messages=conversations[user_id]
        )
        response_content = response.choices[0].message.content.strip()
        message_chunks = [
            response_content[i : i + 2000]
            for i in range(0, len(response_content), 2000)
        ]
        conversations[user_id].append(
            {"role": "assistant", "content": response_content}
        )

        await send_response_chunks(ctx, message_chunks)

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")
