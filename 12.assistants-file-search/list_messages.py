from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def get_thread_messages(client: OpenAI, thread_id: str):
    return client.beta.threads.messages.list(thread_id)


def print_thread_messages(thread_messages):
    for data in thread_messages.data:
        print(f'{data.role}> ', end='')
        for content in data.content:
            print(content.text.value)


if __name__ == '__main__':
    
    client = OpenAI()

    thread_id = "thread_123abc"
    thread_messages = get_thread_messages(client, thread_id)
    print_thread_messages(thread_messages)