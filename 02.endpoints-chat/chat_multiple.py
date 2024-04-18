from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "너가 가장 잘 하는 걸 한 줄로 말해줘."},
  ],
  n=3 # 3개의 답변
)

print(f'답변 개수: {len(completion.choices)}')

for i in range(len(completion.choices)):
  print(f'답변 {i+1}: {completion.choices[i].message.content}')

