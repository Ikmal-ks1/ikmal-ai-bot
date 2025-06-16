import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content
