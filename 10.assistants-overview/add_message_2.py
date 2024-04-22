from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

thread_id = "thread_123abc"
thread = client.beta.threads.retrieve(thread_id)

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I need to solve the equation `2x + 21 = 27`. Can you help me?"
)

# print(message.model_dump_json())