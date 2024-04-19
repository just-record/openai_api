from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-turbo-preview", # gpt-3.5-turbo-0125, gpt-4-turbo-preview
  response_format={ "type": "json_object" },
  messages=[
    # System message에 JSON 형태로 출력 하라는 지침을 줍니다.
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)

print(response.choices[0].message.content)