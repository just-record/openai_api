from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0613",
  messages=[
    {"role": "user", "content": "Hello!"}
  ],
  logprobs=True, # Return logprobs
  top_logprobs=2 # Return top 2 logprobs
)

print(completion.choices[0].message.content)
print('--------------------')
contents = completion.choices[0].logprobs.content
for i, content in enumerate(contents):
    # token: The token that was generated, logprob: The log-probability of the token
    print(f'{i+1} - token: {content.token}, logprob: {content.logprob}') 
    top_logprobs = content.top_logprobs
    # 확률이 높은 상위 2개의 token과 logprobs
    for j, top_logprob in enumerate(top_logprobs):
        print(f'    {j+1} - token: {top_logprob.token}, logprob: {top_logprob.logprob}')
    print('')



# print(completion.choices[0].logprobs)
