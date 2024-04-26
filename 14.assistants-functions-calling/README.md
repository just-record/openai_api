# Tool('Function Calling')을 사용 하여 사용자 함수 호출하기

API: <https://platform.openai.com/docs/api-reference/assistants>

가이드: <https://platform.openai.com/docs/assistants/tools/function-calling/function-calling-beta>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

**openai의 버전을 업그레이드 합니다.**

```bash
# openai의 버전을 업그레이드 합니다.
pip install -U openai
```

## 함수 정의

`define_function.py`: 함수를 정의합니다.

## Thread 생성, Meaasge 추가

### 1. Thread 생성

`create_thread.py`

### 2. Message 추가

`add_message.py`

### 3. Thread의 Message 확인

`list_messages.py`

## Run 생성 및 출력 확인

`run_without_streaming.py`

'requires_action'으로 변경 하는 상태와 함수 호출 상태를 출력 하여 확인합니다.
