from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def create_run(client: OpenAI, thread_id: str, assistant_id: str):
    return client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id
    )


def get_messages(client: OpenAI, thread_id: str, run_id: str):
    return list(client.beta.threads.messages.list(thread_id=thread_id, run_id=run_id))


def get_message_content(messages):
    return messages[0].content[0].text


def get_citations(message_content):
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")
    return citations



if __name__ == '__main__':
    
    client = OpenAI()

    thread_id = "thread_123abc"
    assistant_id = "asst_123abc"

    run = create_run(client, thread_id, assistant_id)
    messages = get_messages(client, thread_id, run.id)

    message_content = get_message_content(messages)
    print(type(message_content))
    citations = get_citations(message_content)

    print(message_content.value)
    print("\n".join(citations))

    