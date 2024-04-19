# OpenAI Endpoints Models

API: <https://platform.openai.com/docs/api-reference/models>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## 모델 목록 조회

`list_models.py`: 모델 목록을 조회합니다.

결과: 모델 목록을 출력합니다. (사용자가 파인 튜닝 하여 생성한 모델도 포함 되어 있습니다.)

```text
모델의 개수: 32
{"id":"gpt-3.5-turbo-16k-0613","created":1685474247,"object":"model","owned_by":"openai"}
{"id":"whisper-1","created":1677532384,"object":"model","owned_by":"openai-internal"}
...
```

## 모델 검색

`retrieve_model.py`: 모델 ID를 이용하여 모델을 검색합니다.

결과:

```text
{"id":"gpt-3.5-turbo-16k-0613","created":1685474247,"object":"model","owned_by":"openai"}
```

## 파인 튜닝 된 모델 삭제

`delete_model.py`: 파인 튜닝 된 모델을 삭제합니다.
