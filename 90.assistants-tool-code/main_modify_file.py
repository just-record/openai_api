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
        model: str = "gpt-4-turbo-2024-04-09",
        file_ids: list = None,):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model,
        file_ids=file_ids,
    )


# 파일 검색
def get_assistant_byid(client: OpenAI, assistant_id: str):
    return client.beta.assistants.retrieve(assistant_id)


### Assistant file 수정
def modify_assistant_files(
        client: OpenAI, 
        assistant_id: str,
        file_ids: list):
    client.beta.assistants.update(
        assistant_id=assistant_id,
        file_ids=file_ids,
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
                    message_history.append(f'Assistant> {content.image_file.file_id}')
        else:
            break
    
    for message in message_history[::-1]:
        print(message)


def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)

def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)   

def delete_file(client: OpenAI, file_id: str):
    client.files.delete(file_id)         


if __name__ == '__main__':
    
    client = OpenAI()

    file_path = './train.csv'
    file = upload_file(client, file_path)
    modify_file_id = ''

    assistant_params = {
        "name": "Data Analysis Expert",
        "instructions": "You are a data analysis expert. Analyze data, generate insights, create visualizations, and run statistical tests. Please provide detailed explanations for each step of your analysis.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-turbo-2024-04-09",
        "file_ids": [file.id]
    }
    assistant = get_assistant(client, **assistant_params)
    thread = get_thread(client)
    
    while True:
        message = get_user_query()
        role = "user"
        if message == "/q":
            print("Quitting...")
            break
        elif message == "/f":       # 파일 변경
            file_path = './netflix.csv'
            modify_file = upload_file(client, file_path)
            modify_file_id = modify_file.id  
            modify_assistant_files(client=client, assistant_id=assistant.id, file_ids=[modify_file_id])
            print(f'You> File has been updated.')
        else:
            add_message_to_thread(client=client, thread_id=thread.id, message=message, role=role)
            print(f'You> {message}')
            run = create_run(client, thread.id, assistant.id)
            run = get_completed_run(client, thread.id, run.id)

            if run.status == "completed":
                print(print_assistant_messages(client, thread.id))
            else:
                print("There is a problem, please try again.")

    delete_assistant(client, assistant.id) 
    delete_thread(client, thread.id)
    delete_file(client, file.id)
    # 파일 삭제
    if modify_file_id:
        delete_file(client, modify_file_id)
    

    









