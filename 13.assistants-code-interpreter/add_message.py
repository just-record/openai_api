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

    query = "성별 생존율을 말해 줘"

    message_params = {
        "thread_id": "thread_123abc",
        "role": "user",
        "message": query,
        "file_id": "file-123abc",
        "tool_type": "code_interpreter",
    }
    add_message_to_thread(client, **message_params)

