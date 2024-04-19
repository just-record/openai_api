from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

moderation = client.moderations.create(input="I want to kill them.")
result = moderation.results[0]

print(result.flagged)
print('-----------')
for key, value in result.categories:
    print(f'{key}:  {value}')
print('-----------')
for key, value in result.category_scores:
    print(f'{key}:  {value}')