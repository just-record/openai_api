from typing import List
from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def upload_file(client: OpenAI, file_path: str):
    return client.files.create(
        file=open(file_path, "rb"),
        purpose="assistants"
    )


def get_assistant(
        client: OpenAI,
        name: str = "Assistant-default",
        instructions: str = "You are a helper assistant. You can help users with their queries.",
        tools: list = [],
        model: str = "gpt-4-turbo"
    ):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model
    )


def get_thread(client: OpenAI):
    return client.beta.threads.create()


# Message 에 file이 attache 되도록 수정
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


def get_user_query():
    return input("Enter a query! (Enter '/q' to quit): ")


def create_run(client: OpenAI, thread_id: str, assistant_id: str):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )


def get_run(client: OpenAI, thread_id: str, run_id: str):
    return client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )


def get_completed_run(client: OpenAI, thread_id: str, run_id: str):
    run = get_run(client, thread_id, run_id)
    while run.status == "queued" or run.status == "in_progress":
        run = get_run(client, thread_id, run_id)
    return run


def print_assistant_messages(client: OpenAI, thread_id: str):
    message_history = []
    thread_messages = client.beta.threads.messages.list(thread_id, order='desc')
    datas = thread_messages.data
    for data in datas:
        if data.role == 'assistant':
            for content in data.content:
                if content.type == 'text' and content.text.value:
                    message_history.append(f'Assistant> {content.text.value}')
                elif content.type == 'image_file' and content.image_file.file_id:
                    message_history.append(f'Assistant> <{content.image_file.filename}> 파일 생성')
        else:
            break
    
    for message in message_history[::-1]:
        print(message)


# Assistant 삭제 
def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)

# Thread 삭제
def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)   

# 업로드 된 File 삭제
def delete_files(client: OpenAI, file_ids: List):
    for file_id in file_ids:
        client.files.delete(file_id)      


if __name__ == '__main__':
    
    client = OpenAI()

    file_paths = ['../resources/train.csv']
    files = [upload_file(client, file_path) for file_path in file_paths]

    assistant_params = {
        "name": "Data Analysis Expert",
        "instructions": "You are a data analysis expert. Analyze data, generate insights, create visualizations, and run statistical tests. Please provide detailed explanations for each step of your analysis.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-turbo"
    }
    assistant = get_assistant(client, **assistant_params)
    thread = get_thread(client)

    # 첫번째 query에서 file을 attach 하도록 수정
    query_cnt = 0
    while True:
        message = get_user_query()
        role = "user"
        if message == "/q":
            print("Quitting...")
            break
        else:
            if query_cnt == 0:
                message_params = {
                    "message": message,
                    "file_id": files[0].id,   # train.csv attach
                    "tool_type": "code_interpreter"
                }
            else:
                message_params = {
                    "message": message
                }            
            # parameters 수정
            add_message_to_thread(client=client, thread_id=thread.id, role=role, **message_params)
            print(f'You> {message}')
            run = create_run(client, thread.id, assistant.id)
            run = get_completed_run(client, thread.id, run.id)

            if run.status == "completed":
                print_assistant_messages(client, thread.id)
            else:
                print("There is a problem, please try again.")

    delete_assistant(client, assistant.id)
    delete_thread(client, thread.id)
    delete_files(client, [file.id for file in files])