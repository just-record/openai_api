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

### Assistants - 기본 사용 하기

`10.assistants-overview` 디렉토리에서 실행합니다. Assistants를 사용하는 기본적인 방법을 연습합니다.

### Assistants - 대화 이어서 하기

`11.assistants-chat` 디렉토리에서 실행합니다. Assistants를 사용하여 대화를 이어서 하는 방법을 연습합니다.

### Tool('code_interpreter')데이터 분석 하기

`12.assistants-tool-code` 디렉토리에서 실행합니다. Tool('code_interpreter')을 사용하여 데이터 분석을 하는 방법을 연습합니다.

### code-interpreter - 기타

`13.assistants-tool-code-files` 디렉토리에서 실행합니다.

- 서로 다른 2개 이상의 파일을 사용하여 질의하기
- 이미지로 답변 받았을 때 처리하기

### file_search - 기본 사용

TODO

### file_search - 2개 이상의 파일을 사용하여 질의하기

TODO

### functions_calling - 2개 이상의 함수를 사용하여 질의하기

TODO

### functions_calling - 시나리오를 작성 하여 질의하기

TODO

### Thread의 전체 목록을 조회 할 수 있나? 없는 것 같은데 Thread는 언제 삭제 되나?

TODO

### 새로 생긴 Vector Store, Vector Store File, Vector Store File Batches

TODO

### Run의 required_action 분석 하기

TODO - 언제 발생 되는지, 어떻게 사용 되는지
