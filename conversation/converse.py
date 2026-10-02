from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv("../.env.local")

client = Groq(api_key=os.environ["GROQ_API_KEY"])

messages = []

print("Conversation started. Type 'quit' to exit.\n")

while True:
    user = input("You: ")

    if user.lower() == "quit":
        break

    messages.append({
        "role": "user",
        "content": user
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
    )

    reply = response.choices[0].message.content

    print(f"AI: {reply}\n")

    messages.append({
        "role": "assistant",
        "content": reply
    })
