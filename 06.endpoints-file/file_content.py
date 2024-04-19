from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

content = client.files.content("file-Vlp0Cbr1INdQd9bj0b4I1kN7")
print(content.content.decode('utf-8')) # bytes to string