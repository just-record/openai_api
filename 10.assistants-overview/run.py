from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import time

client = OpenAI()

assistant_id = "asst_123abc"  # 조금 전 생성한 assistant의 ID를 사용합니다.
assistant = client.beta.assistants.retrieve(assistant_id)
thread_id = "thread_123abc"  # 조금 전 생성한  thread의 ID를 사용합니다.
thread = client.beta.threads.retrieve(thread_id)

# assistant와 thread를 이용 하여 Run을 생성합니다.
run = client.beta.threads.runs.create(
  thread_id = thread.id,
  assistant_id = assistant.id
)

# Run은 비동기적으로 실행되기 때문에, 상태를 계속 모니터링 해야 합니다.
# queue 또는 in_progress 상태일 때는 완료가 되지 않은 상태입니다.
# 해당 Run을 검새하여 완료가 될 때까지 계속 상태를 확인합니다.
while run.status == "queued" or run.status == "in_progress":
    print(run.model_dump_json())
    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    time.sleep(0.5)