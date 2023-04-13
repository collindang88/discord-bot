from ..utils.c_log import log
import openai

@log('contacting gpt')
async def gpt(ctx, *input):    
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