from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! My name is Hong Gildong."},
    {"role": "system", "content": "Hello! How can I assist you today?"},
    {"role": "user", "content": "What is my name?."}
  ]
)

print(completion.choices[0].message.content)
