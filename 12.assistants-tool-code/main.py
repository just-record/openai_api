from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


# 파일 업로드
def upload_file(client: OpenAI, file_path: str):
    return client.files.create(
        file=open(file_path, "rb"),
        # 이 중에서 하나만 가능: 'fine-tune', 'assistants', 'batch', 'user_data', 'responses'
        purpose="assistants"
    )


# Assistant 생성
def get_assistant(
        client: OpenAI,
        name: str = "Assistant-default",
        instructions: str = "You are a helper assistant. You can help users with their queries.",
        tools: list = [],
        model: str = "gpt-4-turbo-2024-04-09",
        file_ids: list = None,):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model,
        file_ids=file_ids,
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
    return input("Enter a query! (Enter '/q' to quit): ")


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

# 파일 삭제
def delete_file(client: OpenAI, file_id: str):
    client.files.delete(file_id)         


if __name__ == '__main__':
    
    client = OpenAI()

    # 파일 업로드
    file_path = './train.csv'
    file = upload_file(client, file_path)  

    assistant_params = {
        "name": "Data Analysis Expert",
        "instructions": "You are a data analysis expert. Analyze data, generate insights, create visualizations, and run statistical tests. Please provide detailed explanations for each step of your analysis.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-turbo-2024-04-09",
        "file_ids": [file.id]
    }
    assistant = get_assistant(client, **assistant_params)   # assistant 생성
    thread = get_thread(client)         # thread 생성
    
    while True:     # 대화 계속 하기
        message = get_user_query()  # ex) 몇 건의 데이터가 있나? 또 몇 개의 항목이 있나? | 생존율을 성별로 말해 줘
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
    delete_file(client, file.id)        # 파일 삭제
    

    









