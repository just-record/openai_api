from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def add_message_to_thread(client: OpenAI, thread_id: str, role: str, message: str, file_id: str):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=message, 
        attachments = [
            {
                "file_id": file_id,
                "tools": [{"type": "file_search"}],
            }
        ]
    )


if __name__ == '__main__':
    
    client = OpenAI()

    query = "백성수의 다른 이름을 말해 줘"

    message_params = {
        "thread_id": "thread_123abc",
        "role": "user",
        "message": query,
        "file_id": "file-123abc",
    }
    add_message_to_thread(client, **message_params)

