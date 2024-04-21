from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()
  
thread = client.beta.threads.create()

print(thread.model_dump_json())

# {"id":"thread_91a5ZaV4Up0i2gXDZzo11LoB","created_at":1713669248,"metadata":{},"object":"thread"}
# {"id":"thread_ASW07mbTGURl6qoQi63bOnm8","created_at":1713672655,"metadata":{},"object":"thread"}