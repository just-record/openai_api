from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()
  
thread = client.beta.threads.create()

print(thread.model_dump_json())