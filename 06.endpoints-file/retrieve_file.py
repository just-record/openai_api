from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
client = OpenAI()

file = client.files.retrieve("file-123abc")

print(file.model_dump_json())