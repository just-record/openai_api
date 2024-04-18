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

### 예제 1

TODO

### 예제 2

TODO
