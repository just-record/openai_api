from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import time
import json


# 챗봇에 의해 생성될 함수의 실제 구현
def get_current_temperature(location: str, unit: str):
    print(f'코드 상의 get_current_temperature 함수 호출됨')
    print(f'location: {location}, unit: {unit}')
    return "31"


# 챗봇에 의해 생성될 함수의 실제 구현
def get_rain_probability(location: str):
    print(f'코드 상의 get_rain_probability 함수 호출됨')
    print(f'location: {location}')
    return "0.08"


# 챗봇에 의해 생성 된 함수의 출력을 가져와서 실제 함수 호출하고 결과를 반환
def get_tool_outputs(run: object):
    tool_outputs = []
    # 'required_action'상태 일 때 tool로 선정 된 함수 정보를 가져 옴
    for tool in run.required_action.submit_tool_outputs.tool_calls:
        if tool.function.name == "get_current_temperature":   # 함수 이름
            arguments = json.loads(tool.function.arguments)   # 함수의 인자
            location = arguments.get('location')
            unit = arguments.get('unit')
            # 실제 함수 호출
            temperature = get_current_temperature(location=location, unit=unit)
            tool_outputs.append({
            "tool_call_id": tool.id,
            "output": temperature   # 실제 함수 호출 결과
            })
        elif tool.function.name == "get_rain_probability":
            arguments = json.loads(tool.function.arguments)
            location = arguments.get('location')
            rain_probability = get_rain_probability(location=location)            
            tool_outputs.append({
            "tool_call_id": tool.id,
            "output": rain_probability
            })
    return tool_outputs


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


# 'requires_action'으로 상태가 변경 되는 과정, 함수 호출 과정을 표시
def display_run(client: OpenAI, thread_id: str, run_id: str):
    previous_run_status = ''
    run = get_run(client, thread_id, run_id)

    while run.status == "queued" or run.status == "in_progress":
        run = get_run(client, thread_id, run_id)
        run_status = run.status
        print(f'run.status: {run_status}')   # run 상태 출력
        if run_status != previous_run_status: # run 상태가 변경 되면 run 정보 출력
            print(f'run: {run.model_dump_json()}')
            previous_run_status = run_status        
        time.sleep(0.5)

    # run이 'queued' 또는 'in_progress' 상태를 벗어 나면
    print(f'after while -> run.status: {run_status}')

    # 'requires_action' 상태 일 때
    if run.status == "requires_action":
        print("Run requires action.")
        # 실제 함수를 실행 시킨 tool_outputs를 값을 가져오기
        tool_outputs = get_tool_outputs(run)
        print(f'tool_outputs: {tool_outputs}')
        # tool_outputs가 있으면 tool_outputs를 제출
        if tool_outputs:
            try:
                # tool_outputs 제출하여 tool의 결과 값으로 사용자에게 답변을 생성
                run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
                print(f'submit_tool_outputs_and_poll ==> run: {run.model_dump_json()}')
                print("Tool outputs submitted successfully.")
            except Exception as e:
                print("Failed to submit tool outputs:", e)
            else:
                print("No tool outputs to submit.")


# 챗봇이 생성한 최종 메시지를 출력
def print_assistant_messages(client: OpenAI, thread_id: str):
    message_history = []
    thread_messages = client.beta.threads.messages.list(thread_id, order='desc')
    datas = thread_messages.data
    for data in datas:
        if data.role == 'assistant':
            for content in data.content:
                if content.type == 'text' and content.text.value:
                    message_history.append(f'Assistant> {content.text.value}')
                elif content.type == 'image_file' and content.image_file.file_id:
                    # download_file(content.image_file.file_id)  # 파일 다운로드는 우선 생략
                    message_history.append(f'Assistant> {content.text.value}')
        else:
            break
    
    for message in message_history[::-1]:
        print(message)

if __name__ == '__main__':
    
    client = OpenAI()

    thread_id = "thread_123abc"
    assistant_id = "asst_123abc"

    run = create_run(client, thread_id, assistant_id)
    display_run(client, thread_id, run.id)
    print(' ' * 20)
    print_assistant_messages(client, thread_id)
