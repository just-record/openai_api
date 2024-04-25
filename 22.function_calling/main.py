import json
from typing import List
from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


# 장비 동작 제어
# equipment_actions = {
#     "light": ["on", "off"],
#     "fan": ["on", "off"],
#     "tv": ["on", "off"],
#     "ac": ["on", "off"],
# }


# 장비 동작 제어 함수
def equipment_control(
    equipment: str,
    action: str,
):
    equipment_action = f'I Turned {action} {equipment}.'
    print(equipment_action)
    return equipment_action


# def upload_file(client: OpenAI, file_path: str):
#     return client.files.create(
#         file=open(file_path, "rb"),
#         purpose="assistants"
#     )


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


def get_run_steps(client: OpenAI, thread_id: str, run_id: str):
    return client.beta.threads.runs.steps.list(
        thread_id=thread_id,
        run_id=run_id
    )


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


# 챗봇에 의해 생성 된 함수의 출력을 가져와서 실제 함수 호출하고 결과를 반환
def get_tool_outputs(run: object):
    tool_outputs = []
    # 'required_action'상태 일 때 tool로 선정 된 함수 정보를 가져 옴
    for tool in run.required_action.submit_tool_outputs.tool_calls:
        if tool.function.name == "equipment_control":   # 함수 이름
            arguments = json.loads(tool.function.arguments)   # 함수의 인자
            equipment = arguments.get('equipment')
            action = arguments.get('action')
            # 실제 함수 호출
            result = equipment_control(equipment=equipment, action=action)
            tool_outputs.append({
                "tool_call_id": tool.id,
                "output": result   # 실제 함수 호출 결과
            })
    return tool_outputs                            


def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)

def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)   

def delete_files(client: OpenAI, file_ids: List):
    for file_id in file_ids:
        client.files.delete(file_id)      


if __name__ == '__main__':
    
    client = OpenAI()

    tools = [
        {
            "type": "function",
            "function": {
                "name": "equipment_control",
                "description": "Identify the user's condition or request and operate the appropriate equipment according to the situation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "equipment": {
                            "type": "string",
                            "enum": ["Light", "Fan", "TV", "AC"],
                            "description": "Equipment such as Light, Fan, TV, AC"
                        },
                        "action": {
                            "type": "string",
                            "enum": ["on", "off"],
                            "description": "The type of operation of the equipment, for example, on, off"
                        }
                    },
                    "required": ["equipment", "action"]
                }
            }
        }
    ]

    assistant_params = {
        "name": "Equipment control bot",
        "instructions": "You are the equipment control bot. Understand requests and use the provided functions to answer questions.",
        "tools": tools,
        "model": "gpt-4-turbo"
    }
    assistant = get_assistant(client, **assistant_params)
    thread = get_thread(client)

    # query_cnt = 0
    while True:
        message = get_user_query()
        role = "user"
        if message == "/q":
            print("Quitting...")
            break
        else:
            message_params = {
                "message": message
            }                            
            add_message_to_thread(client=client, thread_id=thread.id, role=role, **message_params)
            print(f'You> {message}')
            run = create_run(client, thread.id, assistant.id)
            run = get_completed_run(client, thread.id, run.id)

            if run.status == "requires_action":
                # 실제 함수를 실행 시킨 tool_outputs를 값을 가져오기
                tool_outputs = get_tool_outputs(run)
                if tool_outputs:
                    try:
                        # tool_outputs 제출하여 tool의 결과 값으로 사용자에게 답변을 생성
                        run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                            thread_id=thread.id,
                            run_id=run.id,
                            tool_outputs=tool_outputs
                        )
                        # print(f'submit_tool_outputs_and_poll ==> run: {run.model_dump_json()}')
                        # print("Tool outputs submitted successfully.")
                    except Exception as e:
                        print("Failed to submit tool outputs:", e)
                    # else:
                    #     print("No tool outputs to submit.")
            elif run.status == "completed":
                print_assistant_messages(client, thread.id)
            else:
                print("There is a problem, please try again.")
        
    delete_assistant(client, assistant.id)
    delete_thread(client, thread.id)