from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
from event_handler import EventHandler


def get_assistant(client: OpenAI):
    return client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-2024-04-09",
    )


def get_thread(client: OpenAI):
    return client.beta.threads.create()


def add_message_to_thread(client: OpenAI, thread_id: str, message: str, role: str = "user"):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=message,
    )


def get_user_query():
    return input("\nEnter a math question(Enter '/q' to quit): ")


def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)


def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)        


if __name__ == '__main__':
    client = OpenAI()
    assistant = get_assistant(client)
    thread = get_thread(client)
    
    while True:
        message = get_user_query()  # "I need to solve the equation `3x + 11 = 14`. Can you help me?"
        role = "user"
        if message == "/q":
            print("Quitting...")
            break
        else:
            add_message_to_thread(client=client, thread_id=thread.id, message=message, role=role)
            print(f'You> {message}')

            # stream 생성
            with client.beta.threads.runs.stream(
                thread_id=thread.id,
                assistant_id=assistant.id,
                event_handler=EventHandler(),
            ) as stream:
                stream.until_done()

    delete_assistant(client, assistant.id)
    delete_thread(client, thread.id)

    









