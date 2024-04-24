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

    file = create_file(client, file_path='./김동인-광염_소나타-중외일보.pdf', purpose="assistants")

    print(file.model_dump_json())


