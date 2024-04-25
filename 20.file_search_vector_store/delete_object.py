from typing import List
from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

# Assistant 목록 조회
def get_assistants(client: OpenAI, order: str = 'desc', limit: str = '20'):
    return client.beta.assistants.list(
        order=order,
        limit=limit
    )

# Vector Store 목록 조회
def get_vector_stores(client: OpenAI, order: str = 'desc', limit: str = '20'):
    return client.beta.vector_stores.list(
        order=order,
        limit=limit
    )

# File 목록 조회
def get_files(client: OpenAI):
    return client.files.list()

# Assistant 삭제 
def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)


# Vector Stores 삭제
def delete_vector_stores(client: OpenAI, vector_store_ids: List):
    for vector_store_id in vector_store_ids:
        client.beta.vector_stores.delete(vector_store_id)


# File 삭제
def delete_files(client: OpenAI, file_ids: List):
    for file_id in file_ids:
        client.files.delete(file_id)


if __name__ == '__main__':
    
    client = OpenAI()

    assistants = get_assistants(client)
    vector_stores = get_vector_stores(client)
    files = get_files(client)
    
    # Assistant 조회 및 삭제
    print(f'Assistants: {assistants}')
    for assistant in assistants.data:
        print(f'Assistant: {assistant.model_dump_json()}')
        delete_assistant(client, assistant.id)

    # Vector Store 조회 및 삭제
    delete_target_vector_stores = []
    for vector_store in vector_stores.data:
        print(f'Vector Store: {vector_store.model_dump_json()}')
        delete_target_vector_stores.append(vector_store.id)
    delete_vector_stores(client, delete_target_vector_stores)

    # File 조회 및 삭제(assistants 용도만)
    delete_target_files = []
    for file in files.data:
        print(f'Files: {file.model_dump_json()}')

        if file.purpose in ['assistants', 'assistants_output']:
            delete_target_files.append(file.id)
    delete_files(client, delete_target_files)