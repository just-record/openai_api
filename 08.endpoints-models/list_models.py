from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

models = client.models.list().data

print(f'모델의 개수: {len(models)}')
for model in models:
    print(model.model_dump_json())