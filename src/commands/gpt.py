# Third Party
import openai

# First Party
from src.utils.c_log import log

conversations = {}


@log("contacting gpt")
async def gpt(ctx):
    user_id = str(ctx.author.id)
    prompt = ctx.message.content[4:].strip()

    if user_id not in conversations:
        conversations[user_id] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    conversations[user_id].append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0314", messages=conversations[user_id]
        )
        response_content = response.choices[0].message.content.strip()
        message_chunks = [
            response_content[i : i + 2000]
            for i in range(0, len(response_content), 2000)
        ]
        conversations[user_id].append(
            {"role": "assistant", "content": response_content}
        )

        for chunk in message_chunks:
            await ctx.send(chunk)

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")
