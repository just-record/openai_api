from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
client = OpenAI()

file = client.files.retrieve("file-82HVNoRH0qfqb2S3B9VqXVWi")

print(file.model_dump_json())