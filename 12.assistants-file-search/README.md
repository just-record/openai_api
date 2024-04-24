# Tool('File Search')을 사용 하여 파일 내용 질의 하기

API: <https://platform.openai.com/docs/api-reference/assistants>

가이드: <https://platform.openai.com/docs/assistants/tools/file-search/file-search-beta>

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

만료되거나 기증된 저작물: <https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtText.do?menuNo=200019>

`이효석-모밀꽃_필_무렵.pdf`, `김유정-동백꽃-조광`, `김동인-광염_소나타-중외일보`

## Step 1: File Search 가 가능한 Assistants 생성

`create_assistant.py`: Assistants를 생성합니다.

결과: File Search 가능한 Assistants 생성

## Step 2: 파일 업로드하여 Vector Store 생성

`upload_file_create_vector_store.py`: 파일 업로드하고 업로드 된 파일을 Vector Store에 등록합니다.

결과: 파일 업로드 및 Vector Store 생성

## Step 3: Vettor Store를 사용 하도록 Assistants 업데이트

`update_assistant.py`

결과: Assistants 업데이트

## Step 4: Thread 생성, Meaasge 추가

### 1. Thread 생성

`create_thread.py`

### 2. Message에 추가 할 파일 등록

`add_file.py`

### 3. Message 추가

`add_message_to_thread.py`

### 4. Thread의 Message 확인

`list_messages.py`

## Step 5: Run 생성 및 출력 확인

### 스트리밍 출력

`run_with_streaming.py`

### 스트리밍 없이 출력

새로운 Thread를 생성 하여 테스트: `Step 4`의 Thread 생성, Message 추가 만

`run_without_streaming.py`
