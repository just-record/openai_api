from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def add_message_to_thread(client: OpenAI, thread_id: str, role: str, message: str, file_id: str | None = None, tool_type: str | None = None):
    attachments = []
    if file_id:
        attachments = [
            {
                "file_id": file_id,
                "tools": [{"type": tool_type}],
            }
        ]

    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=message, 
        attachments = attachments
    )


if __name__ == '__main__':
    
    client = OpenAI()

    query = "What's the weather in San Francisco today and the likelihood it'll rain?"

    message_params = {
        "thread_id": "thread_123abc",
        "role": "user",
        "message": query,
    }
    add_message_to_thread(client, **message_params)

