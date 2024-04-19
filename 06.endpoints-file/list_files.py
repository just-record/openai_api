from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

files = client.files.list()
for file in files.to_dict()['data']:
  print(file)
