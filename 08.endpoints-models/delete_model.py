from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

model = client.models.delete("davinci:ft-personal-2023-xx-xx-xx-xx-xx")

print(model.model_dump_json())