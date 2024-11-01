from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0613",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "너가 가장 잘 하는 걸 한 줄로 말해줘."},
  ],
  n=3
)

print(completion.usage.to_dict())


