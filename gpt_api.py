import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_TOKEN')

input = ['hi', 'there']
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
    print(response.choices[0].message.content.strip())
except Exception as e:
    print(f"Error: {str(e)}")