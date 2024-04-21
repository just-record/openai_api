# OpenAI Assistants - 기본 사용 하기

API: <https://platform.openai.com/docs/api-reference/assistants>

가이드: <https://platform.openai.com/docs/assistants/overview/agents>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## 1. Assistants 생성

`create_assistants.py`: Assistant를 생성합니다.

결과: Assistant가 생성됩니다. Assistant의 ID를 보관해 둡니다.

## 2. Thread 생성

`create_thread.py`: Thread를 생성합니다.
t
결과: Thread가 생성됩니다. Thread의 ID를 보관해 둡니다.

## 3. Thread에 Message 추가

`add_message.py`: Thread에 Message를 추가합니다.

결과: Thread에 Message가 추가됩니다.

## 4. Thread의 Message 확인

`get_thread_meaasge.py`: Thread의 Message를 확인합니다.

결과: Thread의 Message가 확인됩니다.

## 5. Run 생성

`run.py`: Assistant와  Thread을 이용 하여 Run을 생성합니다.

결과: Run이 생성되고 Run이 완료 될 때까지 모니터링 합니다.

## 6. Message 확인  - Run이 완료 된 후

`get_run_message.py`: Run의 Message를 확인합니다.

결과: Assistant의 답변이 있는 Thread의 Message가 확인됩니다.

```text
<assistant>
The solution to the equation \(3x + 11 = 14\) is \(x = 1\).
------
<assistant>
Certainly! Let's solve the equation \(3x + 11 = 14\).

First, we will isolate \(x\) by performing operations on both sides of the equation. Here's how you do it step-by-step:

1. Subtract 11 from both sides to eliminate the constant term on the left side.
2. Divide both sides by 3 to solve for \(x\).

Let me calculate that for you.
------
<user>
I need to solve the equation `3x + 11 = 14`. Can you help me?
------
```

## 7. Stream 사용 하기

### 7.1. Thread에 Message 추가

`add_message_2.py`: Thread에 Message를 추가합니다.

### 7.2. Message 확인

`get_thread_meaasge.py`: Thread의 Message를 확인합니다.

### 7.3. Run

`run_event_handler.py`: Run을 stream 합니다.

결과: Assistant의 답변이 Streaming 됩니다.
