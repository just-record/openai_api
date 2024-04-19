from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

file = client.files.delete("file-w0yiSpyN8zrnybv0CXYAXUMk")

print(file.model_dump_json())