import requests
import json
from groq import Groq

import config

example = ""

# Initialize OpenAI API key
client = Groq(
    api_key=config.get_groq_key()
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": example,
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)