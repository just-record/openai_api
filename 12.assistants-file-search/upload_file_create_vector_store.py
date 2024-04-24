from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

def create_vector_store(client: OpenAI, name: str):
    return client.beta.vector_stores.create(
        name=name
    )


def get_file_batch(client: OpenAI, vector_store_id: str, file_paths: list):
    file_streams = [open(file_path, 'rb') for file_path in file_paths]
    return client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store_id, files=file_streams
    )
    

if __name__ == '__main__':
    
    client = OpenAI()

    vector_store_name = "Data Query Expert"
    vector_store = create_vector_store(client, name=vector_store_name)

    file_paths = ['./이효석-모밀꽃_필_무렵.pdf', './김유정-동백꽃-조광.pdf']
    file_batch = get_file_batch(client, vector_store.id, file_paths)

    print(f'file_batch.status: {file_batch.status}')
    print(f'file_batch.file_counts: {file_batch.file_counts}')

    print(vector_store.model_dump_json())