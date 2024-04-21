# OpenAI Assistants - 대화 이어서 하기

API: <https://platform.openai.com/docs/api-reference/assistants>

가이드: <https://platform.openai.com/docs/assistants/overview/agents>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## 대화 이어서 하기

`main.py`: 실행 파일

계속 해서 대화를 이어 갈 수 있습니다. 이전 대화의 내용을 기억합니다. `/q`를 입력하면 대화를 종료합니다.

## 스트리밍 하기

`main_stream.py`: 실행 파일

`event_handler.py`: 이벤트 핸들러를 정의합니다.

대화의 출력을  스트리밍 합니다.
