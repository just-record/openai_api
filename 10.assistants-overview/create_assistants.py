from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()
  
assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4-turbo-2024-04-09",
)

print(assistant.model_dump_json())