from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def create_file(client: OpenAI, file_path: str, purpose: str):
    return client.files.create(
        file=open(file_path, 'rb'),
        purpose=purpose
    )


if __name__ == '__main__':
    
    client = OpenAI()

    file = create_file(client, file_path='../resources/train.csv', purpose="assistants")

    print(file.model_dump_json())


