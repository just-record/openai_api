from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def create_thread(client: OpenAI):
    return client.beta.threads.create()


if __name__ == '__main__':
    
    client = OpenAI()

    thread = create_thread(client)

    print(thread.model_dump_json())
