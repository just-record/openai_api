# OpenAI의 API 사용법 익히기

OpenAI의 API를 사용하기 위해 Python 라이브러리를 설치합니다.

```bash
pip install -U openai
```

API 키를 환경 변수에 설정하고 불러 옵니다.

Python에서 환경 번수를 사용하기 위해 `python-dotenv` 라이브러리를 설치합니다.

```bash
pip install python-dotenv
```

환경 변수를 저장 할 `.env` 파일을 생성하고 아래와 같이 API 키를 입력합니다.

```shell
OPENAI_API_KEY=sk-...
```

Python 코드에서 API 키를 불러옵니다.

```python
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

openai = OpenAI()
...
```

## Endpoints

API: <https://platform.openai.com/docs/api-reference/audio>

### Audio

`01.endpoints-audio` 디렉토리에서 실행합니다.

### Chat

`02.endpoints-chat` 디렉토리에서 실행합니다.

### Embeddings

`03.endpoints-embeddings` 디렉토리에서 실행합니다.

### Fine-tunnig

TODO
<!-- `04.endpoints-fine-tuning` 디렉토리에서 실행합니다. -->

### Batch

TODO
<!-- `05.endpoints-batch` 디렉토리에서 실행합니다. -->

### File

`06.endpoints-file` 디렉토리에서 실행합니다.

### Images

`07.endpoints-images` 디렉토리에서 실행합니다.

### Models

`08.endpoints-models` 디렉토리에서 실행합니다.

### Moderations

`09.endpoints-moderations` 디렉토리에서 실행합니다.

## Assistants

API: <https://platform.openai.com/docs/api-reference/assistants>

**문서를 작성 하는 동안 Assistants의 version이 변경 되었습니다. 작성하던 문서는 'V1'으로 그대로 두고 새롭게 작성하겠습니다.**

```bash
# openai의 버전을 업그레이드 합니다.
pip install -U openai
```

### Assistants - 기본 사용 하기

`10.assistants-overview` 디렉토리에서 실행합니다. Assistants를 사용하는 기본적인 방법을 연습합니다.

### Assistants - 대화 이어서 하기

`11.assistants-chat` 디렉토리에서 실행합니다. Assistants를 사용하여 대화를 이어서 하는 방법을 연습합니다.

### Assistants - File Search

`12.assistants-file-search` 디렉토리에서 실행합니다. 모델 외부의 지식을 사용하여 질의하는 방법을 연습합니다.

### Assistants - Code Interpreter

`13.assistants-code-interpreter` 디렉토리에서 실행합니다. 샌드박스된 실행 환경에서 Python 코드를 작성 하고 실행하는 방법을 연습합니다.

### Assistants - Functions Calling

`14.assistants-functions-calling` 디렉토리에서 실행합니다. 함수를 설명 하고 설명 된 함수 형태로 반환 값을 받아 사용하는 방법을 연습합니다.

## Assistants - 연습

### File Search

`20.file_search_vector_store` 디렉토리에서 실행합니다. File Search에 대해 여러가지 테스트를 합니다.

### Code Interpreter

`21.code_interpreter` 디렉토리에서 실행합니다. Code Interpreter에 대해 여러가지 테스트를 합니다.

## Assistants - V1

### Tool('code_interpreter')데이터 분석 하기

`90.assistants-tool-code` 디렉토리에서 실행합니다. Tool('code_interpreter')을 사용하여 데이터 분석을 하는 방법을 연습합니다.

### code-interpreter - 기타

`91.assistants-tool-code-files` 디렉토리에서 실행합니다.

- 서로 다른 2개 이상의 파일을 사용하여 질의하기
- 이미지로 답변 받았을 때 처리하기

### file_search - 기본 사용

`92.assistants-tool-file-search` 디렉토리에서 실행합니다. file_search를 사용하여 질의하는 방법을 연습합니다.
