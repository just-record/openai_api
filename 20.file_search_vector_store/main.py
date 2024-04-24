from typing import List
from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


# Vector Store 생성
def create_vector_store(client: OpenAI, name: str):
    return client.beta.vector_stores.create(
        name=name
    )


# 파일 업로드 및 Vector Store에 embedding
def get_file_batch(client: OpenAI, vector_store_id: str, file_paths: list):
    file_streams = [open(file_path, 'rb') for file_path in file_paths]
    return client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store_id, files=file_streams
    )


# Assistant 생성
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


# Assistant의 Vector Store 업데이트
def update_assistant_vetcot_store_ids(
        client: OpenAI,
        assistant_id: str,
        vector_store_ids: list,
        ):
    return client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources = {"file_search": {"vector_store_ids": vector_store_ids}}
    )


# Thread 생성
def get_thread(client: OpenAI):
    return client.beta.threads.create()


# Thread에 Message 추가
def add_message_to_thread(client: OpenAI, thread_id: str, message: str, role: str = "user"):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=message,
    )


# User Query 입력 받기
def get_user_query():
    return input("Enter a query! (Enter '/q' to quit): ")


# Run 생성
def create_run(client: OpenAI, thread_id: str, assistant_id: str):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )


# Run 조회
def get_run(client: OpenAI, thread_id: str, run_id: str):
    return client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )


# Run이 완료 될 때까지 기다렸다가 가져 오기
def get_completed_run(client: OpenAI, thread_id: str, run_id: str):
    run = get_run(client, thread_id, run_id)
    while run.status == "queued" or run.status == "in_progress":
        run = get_run(client, thread_id, run_id)
    return run


# 챗봇이 생성이 최종 Message 출력
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


# Assistant 삭제 
def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)

# Thread 삭제
def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)   

# Vector Stores 삭제
def delete_vector_stores(client: OpenAI, vector_store_ids: List):
    for vector_store_id in vector_store_ids:
        client.beta.vector_stores.delete(vector_store_id)


if __name__ == '__main__':
    
    client = OpenAI()

    vector_store_name = "Data Query Expert"
    vector_store = create_vector_store(client, name=vector_store_name)

    file_paths = ['../resources/이효석-모밀꽃_필_무렵.pdf']
    file_batch = get_file_batch(client, vector_store.id, file_paths)


    # Assistant 내용 변경
    assistant_params = {
        "name": "Data Query Expert",
        "instructions": "You are an expert in searching and retrieving information from files. Please efficiently search through the files to find and extract information as requested, answer specific data-related queries, and provide clear explanations for your findings.",
        "tools": [{"type": "file_search"}],
        "model": "gpt-4-turbo"
    }
    assistant = get_assistant(client, **assistant_params)
    vector_store_ids = [vector_store.id]
    update_assistant_vetcot_store_ids(client, assistant.id, vector_store_ids)
    thread = get_thread(client)
    
    while True:
        message = get_user_query()
        role = "user"
        if message == "/q":
            print("Quitting...")
            break
        else:
            add_message_to_thread(client=client, thread_id=thread.id, message=message, role=role)
            print(f'You> {message}')
            run = create_run(client, thread.id, assistant.id)
            run = get_completed_run(client, thread.id, run.id)

            if run.status == "completed":
                print_assistant_messages(client, thread.id)
            else:
                print("There is a problem, please try again.")

    delete_assistant(client, assistant.id)
    delete_thread(client, thread.id)
    delete_vector_stores(client, vector_store_ids)