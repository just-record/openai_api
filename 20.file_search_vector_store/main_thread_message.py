from typing import List
from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

# 파일 업로드
def upload_file(client: OpenAI, file_path: str):
    return client.files.create(
        file=open(file_path, "rb"),
        purpose="assistants"
    )

def create_vector_store(client: OpenAI, name: str):
    return client.beta.vector_stores.create(
        name=name
    )


def get_file_batch(client: OpenAI, vector_store_id: str, file_paths: list):
    file_streams = [open(file_path, 'rb') for file_path in file_paths]
    return client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store_id, files=file_streams
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


def update_assistant_vetcot_store_ids(
        client: OpenAI,
        assistant_id: str,
        vector_store_ids: list,
        ):
    return client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources = {"file_search": {"vector_store_ids": vector_store_ids}}
    )


def get_thread(client: OpenAI):
    return client.beta.threads.create()


def update_thread_tool_resources(client: OpenAI, thread_id: str, tool_resources: dict):
    return client.beta.threads.update(
        thread_id=thread_id,
        tool_resources=tool_resources
    )	


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
                    message_history.append(f'Assistant> {content.image_file.file_id}')
        else:
            break
    
    for message in message_history[::-1]:
        print(message)


def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)

def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)   

def delete_vector_stores(client: OpenAI, vector_store_ids: List):
    for vector_store_id in vector_store_ids:
        client.beta.vector_stores.delete(vector_store_id)

# # Vector Store 파일 삭제
# def delete_vector_store_files(client: OpenAI, vector_store_id: str, file_batch_ids: List):
#     for file_batch_id in file_batch_ids:
#         client.beta.vector_stores.file_batches.cancel(
#             vector_store_id=vector_store_id,
#             batch_id=file_batch_id
#         )

# 업로드 된 File 삭제
def delete_files(client: OpenAI, file_ids: List):
    for file_id in file_ids:
        client.files.delete(file_id)        


if __name__ == '__main__':
    
    client = OpenAI()

    vector_store_names = ["Data Query Expert - Assistant", "Data Query Expert - Thread"] 
    vector_stores = [create_vector_store(client, name=vector_store_name) for vector_store_name in vector_store_names]

    file_paths = [['../resources/이효석-모밀꽃_필_무렵.pdf'], ['../resources/김유정-동백꽃-조광.pdf']]
    file_batchs = [get_file_batch(client, vector_store.id, file_paths[i]) for i, vector_store in enumerate(vector_stores)]
        

    # Message에 file이 attache 되도록 파일 업로드
    message_file_paths = ['../resources/김동인-광염_소나타-중외일보.pdf', '../resources/현진건-운수좋은날+B3356-개벽.pdf']
    files = [upload_file(client, file_path) for file_path in message_file_paths]
    
    assistant_params = {
        "name": "Data Query Expert",
        "instructions": "You are an expert in searching and retrieving information from files. Please efficiently search through the files to find and extract information as requested, answer specific data-related queries, and provide clear explanations for your findings.",
        "tools": [{"type": "file_search"}],
        "model": "gpt-4-turbo"
    }
    assistant = get_assistant(client, **assistant_params)
    update_assistant_vetcot_store_ids(client, assistant.id, [vector_stores[0].id])
    thread = get_thread(client)
    update_thread_tool_resources(client, thread.id, {"file_search": {"vector_store_ids": [vector_stores[1].id]}})
    
    # 첫번째와 다섯번째 query에는 각각 다른 file을 attach 함
    # 여섯번째 query에는 첫번째 파일 내용을 질의 함(다른 파일을 message에 attach하면 대체 되는지 확인)
    query_cnt = 0
    while True:
        message = get_user_query()
        role = "user"
        if message == "/q":
            print("Quitting...")
            break
        else:
            # '김동인-광염_소나타-중외일보.pdf' file을 첫번째 query에 attach
            if query_cnt == 0:
                message_params = {
                    "message": message,
                    "file_id": files[0].id,
                    "tool_type": "file_search"
                }
            # '현진건-운수좋은날+B3356-개벽.pdf' file을 다섯번째 query에 attach
            elif query_cnt == 4:
                message_params = {
                    "message": message,
                    "file_id": files[1].id,
                    "tool_type": "file_search"
                }
            else:
                message_params = {
                    "message": message
                }

            add_message_to_thread(client=client, thread_id=thread.id, role=role, **message_params)
            print(f'You> {message}')
            run = create_run(client, thread.id, assistant.id)
            run = get_completed_run(client, thread.id, run.id)

            if run.status == "completed":
                print_assistant_messages(client, thread.id)
            else:
                print("There is a problem, please try again.")
            
        query_cnt += 1

    delete_assistant(client, assistant.id)
    delete_thread(client, thread.id)
    # for i, vector_store in enumerate(vector_stores):
    #     delete_vector_store_files(client, vector_store.id, [file_batchs[i].id])
    delete_vector_stores(client, [vector_store.id for vector_store in vector_stores])
    delete_files(client, [file.id for file in files])