from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

from typing_extensions import override
from openai import AssistantEventHandler
 
# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.
 
class EventHandler(AssistantEventHandler):    
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)
      
    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)
      
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)
  
    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print(f"\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)

client = OpenAI()

assistant_id = "asst_123abc"
assistant = client.beta.assistants.retrieve(assistant_id)
thread_id = "thread_123abc"
thread = client.beta.threads.retrieve(thread_id)

# stream 생성 - event_handler를 사용하여 response stream을 처리
with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    event_handler=EventHandler(),
) as stream:
    stream.until_done()