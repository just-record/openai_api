# OpenAI Endpoints Files

API: <https://platform.openai.com/docs/api-reference/files>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## 파일 업로드

`upload_file.py`: 파일을 업로드 합니다. 타이타닉 훈련용 데이터셋을 업로드 합니다. 추후 Assistants의 분석 데이터로 사용 하겠습니다.

결과: 파일이 업로드 되고 파일의 정보를 출력합니다.

```text
{'id': 'file-123abc', 'bytes': 61194, 'created_at': 1700000000, 'filename': 'train.csv', 'object': 'file', 'purpose': 'assistants', 'status': 'processed', 'status_details': None}
```

## 파일 목록 조회

`list_files.py`: 업로드 된 파일 목록을 조회합니다.

결과: 업로드 된 파일 목록을 출력합니다.

```text
{'id': 'file-123abc', 'bytes': 61194, 'created_at': 1700000000, 'filename': 'train.csv', 'object': 'file', 'purpose': 'assistants', 'status': 'processed', 'status_details': None}
{'id': 'file-123def', 'bytes': 61194, 'created_at': 1700000001, 'filename': 'valid.csv', 'object': 'file', 'purpose': 'assistants', 'status': 'processed', 'status_details': None}
```

## 파일 조회

`retrieve_file.py`: 파일 ID를 이용 하여 파일을 조회합니다.

결과: 파일의 정보를 출력합니다.

```text
{'id': 'file-123abc', 'bytes': 61194, 'created_at': 1700000000, 'filename': 'train.csv', 'object': 'file', 'purpose': 'assistants', 'status': 'processed', 'status_details': None}
```

## 파일 삭제

`delete_file.py`: 파일 ID를 이용하여 파일을 삭제합니다.

결과: 파일이 삭제되었음을 출력합니다.

```text
{"id":"file-123abc","deleted":true,"object":"file"}
```

## 파일 콘텐츠 검색

`file_content.py`: 파일 ID를 이용하여 파일의 콘텐츠를 조회합니다. `assistants`용 파일은 콘텐츠를 조회할 수 없습니다. `fine-tune`용 파일은 조회 되는걸 확인 했습니다.

결과: 파일의 콘텐츠를 출력합니다.

```text
파일의 콘텐츠: This is a test file.
```
