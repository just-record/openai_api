from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


# Assistant 생성
def get_assistant(client: OpenAI):
    return client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-2024-04-09",
    )


# Thread 생성
def get_thread(client: OpenAI):
    return client.beta.threads.create()


# Message 추가
def add_message_to_thread(client: OpenAI, thread_id: str, message: str, role: str = "user"):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=message,
    )


# 사용자에게 질문 받기 (/q 입력시 종료)
def get_user_query():
    return input("Enter a math question(Enter '/q' to quit): ")


# Run 생성
def create_run(client: OpenAI, thread_id: str, assistant_id: str):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )


# Run 조회
def get_run(client: OpenAI, thread_id: str, run_id: str):
    return client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )


# 모니터링 하다가 완료되면 Run 가져오기
def get_completed_run(client: OpenAI, thread_id: str, run_id: str):
    run = get_run(client, thread_id, run_id)
    while run.status == "queued" or run.status == "in_progress":
        run = get_run(client, thread_id, run_id)
    return run


# Assistant 메시지 출력
def print_assistant_messages(client: OpenAI, thread_id: str):
    # thread_messages = client.beta.threads.messages.list(thread_id, order='asc')
    message_history = []
    thread_messages = client.beta.threads.messages.list(thread_id, order='desc')
    datas = thread_messages.data
    for data in datas:
        if data.role == 'assistant':
            for content in data.content:
                if content.type == 'text' and content.text.value:
                    message_history.append(f'Assistant> {content.text.value}')
                elif content.type == 'image_file' and content.image_file.file_id:
                    message_history.append(f'Assistant> {content.image_file.file_id}')
        else:
            break
    
    for message in message_history[::-1]:
        print(message)


# Assistant 삭제
def delete_assistant(client: OpenAI, assistant_id: str):
    client.beta.assistants.delete(assistant_id)

# Thread 삭제
def delete_thread(client: OpenAI, thread_id: str):
    client.beta.threads.delete(thread_id)        


if __name__ == '__main__':
    client = OpenAI()
    assistant = get_assistant(client)   # assistant 생성
    thread = get_thread(client)         # thread 생성
    
    while True:     # 대화 계속 하기
        message = get_user_query()  # "I need to solve the equation `3x + 11 = 14`. Can you help me?"
        role = "user"
        if message == "/q":         # /q 입력시 종료    
            print("Quitting...")
            break
        else:
            add_message_to_thread(client=client, thread_id=thread.id, message=message, role=role)  # message 추가
            print(f'You> {message}')
            run = create_run(client, thread.id, assistant.id)   # run 생성
            run = get_completed_run(client, thread.id, run.id)  # run 완료되면 가져오기

            # Run의 상태가 정상적으로 완료되면 메시지 출력
            if run.status == "completed":
                print(print_assistant_messages(client, thread.id))
            else:
                print("There is a problem, please try again.")

    delete_assistant(client, assistant.id)  # Assistant 삭제        
    delete_thread(client, thread.id)    # Thread 삭제       

    









