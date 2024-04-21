from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

thread_id = "thread_ASW07mbTGURl6qoQi63bOnm8"  # 조금 전 생성한  thread의 ID를 사용합니다.
thread = client.beta.threads.retrieve(thread_id)

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

print(message.model_dump_json())

# {"id":"msg_AO8XZ3EKmd16iHN6YE3XgNOr","assistant_id":null,"completed_at":null,"content":[{"text":{"annotations":[],"value":"I need to solve the equation `3x + 11 = 14`. Can you help me?"},"type":"text"}],"created_at":1713672722,"file_ids":[],"incomplete_at":null,"incomplete_details":null,"metadata":{},"object":"thread.message","role":"user","run_id":null,"status":null,"thread_id":"thread_ASW07mbTGURl6qoQi63bOnm8"}