# Tool('Code Interpreter')을 사용 하여 파일 내용 질의 하기

API: <https://platform.openai.com/docs/api-reference/assistants>

가이드: <https://platform.openai.com/docs/assistants/tools/code-interpreter>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

**openai의 버전을 업그레이드 합니다.**

```bash
# openai의 버전을 업그레이드 합니다.
pip install -U openai
```

## 자료

- `train.csv`: <https://www.kaggle.com/hesh97/titanicdataset-traincsv/data> - kaggle의 Titanic 데이터셋
- `netflix.csv`: <https://www.kaggle.com/datasets/yaminh/netflix-dataset-for-analysis?select=netflix.csv> - kaggle의 Netflix 데이터셋

## Step 1: Code Interpreter가 가능한 Assistants 생성

`create_assistant.py`: Assistants를 생성합니다.

## Step 2: Thread 생성, Meaasge 추가

### 1. Thread 생성

`create_thread.py`

### 2. Message에 추가 할 파일 등록

`add_file.py`

### 3. Message 추가

`add_message.py`

### 4. Thread의 Message 확인

`list_messages.py`

## Step 3: Run 생성 및 출력 확인

`run_with_streaming.py`
