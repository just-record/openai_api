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

### Chat

### Embeddings

### Fine-tunnig

### Batch

### File

### Images

### Models

### Moderations

## Assistants

### 예제 1

### 예제 2
