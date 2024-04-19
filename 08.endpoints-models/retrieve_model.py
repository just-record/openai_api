from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

model = client.models.retrieve("gpt-3.5-turbo-16k-0613")

print(model.model_dump_json())