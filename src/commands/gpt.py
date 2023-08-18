from src.utils.c_log import log
import openai

@log('contacting gpt')
async def gpt(ctx):
    prompt = ctx.message.content[4:].strip()

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0314",
            messages=messages
        )
        response_content = response.choices[0].message.content.strip()
        message_chunks = [response_content[i:i + 2000] for i in range(0, len(response_content), 2000)]

        for chunk in message_chunks:
            await ctx.send(chunk)
            
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

