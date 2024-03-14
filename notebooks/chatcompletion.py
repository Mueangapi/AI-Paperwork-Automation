import os
from dotenv import load_dotenv
from openai import OpenAI


def chat_completion(prompt):
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt
    )
    return response.choices[0].text

