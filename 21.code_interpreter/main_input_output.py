from typing import List
from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


def upload_file(client: OpenAI, file_path: str):
    return client.files.create(
        file=open(file_path, "rb"),
        purpose="assistants"
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


def get_thread(client: OpenAI):
    return client.beta.threads.create()


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


def download_file(file_id: str, file_type: str = 'image'):
    file = client.files.retrieve(file_id)
    file_content = client.files.content(file_id)
    if file_type == 'image':
        file_name = f'{file.filename}.png'
    else:
        file_name = file.filename.split('.')[0].split('/')[-1] + '.' + file.filename.split('.')[-1]
    with open(f'{file_name}', 'wb') as f:
        f.write(file_content.content)


def get_files_from_message(annotations):
    file_ids = []
    for annotation in annotations:
        if annotation.file_path:
            file_ids.append(annotation.file_path.file_id)
    return file_ids


def print_assistant_messages(client: OpenAI, thread_id: str):
    message_history = []
    thread_messages = client.beta.threads.messages.list(thread_id, order='desc')
    datas = thread_messages.data
    for data in datas:
        if data.role == 'assistant':
            for content in data.content:
                if content.type == 'text' and content.text.value:
                    message_history.append(f'Assistant> {content.text.value}')
                    if content.text.annotations:
                        file_ids = get_files_from_message(content.text.annotations)
                        for file_id in file_ids:
                            download_file(file_id=file_id, file_type='txt')
                elif content.type == 'image_file' and content.image_file.file_id:
                    message_history.append(f'Assistant> <{content.image_file.file_id}> 파일 생성')
                    download_file(content.image_file.file_id)
        else:
            break
    
    for message in message_history[::-1]:
        print(message)


# Run의 steps 가져오기
def get_run_steps(client: OpenAI, thread_id: str, run_id: str):
    return client.beta.threads.runs.steps.list(
        thread_id=thread_id,
        run_id=run_id
    )


# run_steps에서 code_interpreter의 input, output 출력
def print_code_interpreter_in_out(run_steps: List):
    for step in run_steps.data:
        if hasattr(step.step_details, 'tool_calls'):
            tool_calls = step.step_details.tool_calls
            if tool_calls:
                for tool_call in tool_calls:
                    print(f'Input>')
                    print(f'{tool_call.code_interpreter.input}')
                    for output in tool_call.code_interpreter.outputs:
                        if hasattr(output, 'logs'):
                            print(f'Output>')
                            print(f'{output.logs}')


def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)

def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)   

def delete_files(client: OpenAI, file_ids: List):
    for file_id in file_ids:
        client.files.delete(file_id)      


if __name__ == '__main__':
    
    client = OpenAI()

    file_paths = ['../resources/train.csv']
    files = [upload_file(client, file_path) for file_path in file_paths]

    assistant_params = {
        "name": "Data Analysis Expert",
        "instructions": "You are a data analysis expert. Analyze data, generate insights, create visualizations, and run statistical tests. Please provide detailed explanations for each step of your analysis.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-turbo"
    }
    assistant = get_assistant(client, **assistant_params)
    thread = get_thread(client)

    query_cnt = 0
    while True:
        message = get_user_query()
        role = "user"
        if message == "/q":
            print("Quitting...")
            break
        # code interpreter의 input, output 보기
        elif query_cnt != 0 and message == "/l":
            run_steps = get_run_steps(client, thread.id, run.id)
            print_code_interpreter_in_out(run_steps)
        else:
            if query_cnt == 0:
                message_params = {
                    "message": message,
                    "file_id": files[0].id,   # train.csv attach
                    "tool_type": "code_interpreter"
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
                # print(f'Code Interpreter의 Input, Output 보기')
                # run_steps = get_run_steps(client, thread.id, run.id)
                # print_code_interpreter_in_out(run_steps)                
            else:
                print("There is a problem, please try again.")
        
        query_cnt += 1

    delete_assistant(client, assistant.id)
    delete_thread(client, thread.id)
    delete_files(client, [file.id for file in files])