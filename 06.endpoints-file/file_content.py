from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

content = client.files.content("file-123abc")
print(content.content.decode('utf-8')) # bytes to string