from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

def update_assistant_vetcot_store_ids(
        client: OpenAI,
        assistant_id: str,
        vector_store_ids: list,
        ):
    return client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources = {"file_search": {"vector_store_ids": vector_store_ids}}
    )
    

if __name__ == '__main__':
    
    client = OpenAI()

    assistant_id = "asst_123abc"
    vector_store_ids = ["vs_123abc"]

    assistant = update_assistant_vetcot_store_ids(client, assistant_id, vector_store_ids)

    print(assistant.model_dump_json())