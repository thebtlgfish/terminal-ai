import os
from dotenv import load_dotenv
from ollama import Client
from balance import usage
import time

load_dotenv()
api_key = os.getenv('API_KEY')
account_usage = usage(api_key)
print(account_usage)
time.sleep(2)

models = [
    "beam",
    "gemma4:31b",
    "gpt-oss:120b",
    "gpt-oss:20b",
    "nemotron-3-nano:30b",
    "nemotron-3-super",
    "nemotron-3-ultra",
]

for index, model in enumerate(models, 1):
    print(f"{index}. {model}")

choice = int(input("Which Model Do You Want To Use: "))
selected_model = models[choice - 1]

if not api_key:
  raise ValueError(
      "Api Key Not Found"
  )

client = Client(
    host='https://ollama.com', headers={'Authorization': f'Bearer {api_key}'}
)

messages = []

while True:
    message = input("How Can I Cook: ")
    if message.lower() in ['exit', 'quit', 'bye']:
        break

    messages.append({
        'role': 'user',
        'content': message,
    })

    response = client.chat(
        model=selected_model,
        messages=messages,
    )

    assistant_content = response['message']['content']
    print(assistant_content)

    messages.append({
        'role': 'assistant',
        'content': assistant_content,
    })
