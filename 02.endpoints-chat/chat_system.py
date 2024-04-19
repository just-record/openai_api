from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0613",
  messages=[
    {"role": "system", "content": "Please translate it into English."},
    {"role": "user", "content": "안녕하세요. 반갑습니다."}
  ]
)

print(completion.choices[0].message.content)
