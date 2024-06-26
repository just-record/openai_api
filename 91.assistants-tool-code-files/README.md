# Tool('code_interpreter')을 사용 하여 데이터 분석 하기

API: <https://platform.openai.com/docs/api-reference/assistants>

가이드: <https://platform.openai.com/docs/assistants/overview/agents>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## 2개의 csv 파일을 업로드 하고 질문 하기

`main.py`: '타이타닉'과 '넷플릭스' 자료를 업로드. 파일 구분을 하지 않고 질문하기

질문:

- 몇 개의 항목과 몇 건의 데이터가 있는지 알려줘. -> 2개의 파일 각각 알려 줌
- 생존율을 성별로 말해줘. -> '타이타닉' 파일에서만 성별로 생존율을 알려 줌
- 분류별 평점을 말해줘. -> '넷플릭스' 파일에서만 분류별 평점을 알려 줌
- 가장 나이가 많은 생존자의 이름은? -> '타이타닉' 파일에서만 가장 나이가 많은 생존자의 이름을 알려 줌
- 가장 평점이 높은 영화의 제목과 주연 배우, 상영시간을 말해줘. -> '넷플릭스' 파일에서만 가장 평점이 높은 영화의 정보를 알려 줌

결과: 어떤 파일에 대한 질문인지 알 수 없는 경우는 각각 파일에 대한 답변을 하고 알 수 있는 경우는 해당 파일에 대한 답변을 합니다.

## 답변에 이미지가 포함 되었을 때 처리하기

`main_message_image.py`: 그래프를 보여 달라는 질의를 하고 이미지를 처리합니다.

질문:

- 성별에 따른 생존율을 막대 그래프로 보여줘.
