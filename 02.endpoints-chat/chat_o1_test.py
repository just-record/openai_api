from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="o1-preview",
  messages=[
    {"role": "user", "content": "조선 시대와 고려 시대의 문화적 차이점을 정치, 예술, 사회적 관점에서 비교하여 설명해 주세요. 각각의 시대에서 대표적인 인물과 사건을 예로 들어 구체적으로 서술하고, 이러한 차이가 한국 역사에 미친 영향을 간략하게 분석해 주세요."},
  ],
)

print(completion.choices[0].message.content)

print('*'*30)

completion = client.chat.completions.create(
  model="o1-mini",
  messages=[
    {"system": "You are a helpful assistant."},
    {"role": "user", "content": "초등학생을 대상으로 하는 글로, 독서의 중요성에 대해 간단하고 재미있게 설명해 주세요. 독서가 창의력, 상상력, 그리고 학습에 어떤 도움을 주는지 초점을 맞춰 주세요."},
  ],
)

print(completion.choices[0].message.content)