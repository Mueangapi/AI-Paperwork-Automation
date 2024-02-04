import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('api.env')
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def chat_completion(prompt):
    response = client.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        stop=None
    )
    return response.choices[0].text.strip()

prompt = "test"
response = chat_completion(prompt)
print(response)