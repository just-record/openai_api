from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

def get_assistant(
        client: OpenAI,
        name: str = "Assistant-default",
        instructions: str = "You are a helper assistant. You can help users with their queries.",
        tools: list = [],
        model: str = "gpt-4-turbo",
        file_ids: list = None,):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model,
        file_ids=file_ids,
    )

if __name__ == '__main__':
    
    client = OpenAI()

    assistant_params = {
        "name": "Data Query Expert",
        "instructions": "You are an expert in searching and retrieving information from files. Please efficiently search through the files to find and extract information as requested, answer specific data-related queries, and provide clear explanations for your findings.",
        "tools": [{"type": "retrieval"}], # V2에서 file_search가 retrieval로 변경됨
        "model": "gpt-4-turbo"
    }
    assistant = get_assistant(client, **assistant_params)

    print(assistant.model_dump_json())