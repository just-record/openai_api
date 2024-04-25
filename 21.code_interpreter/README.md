# Code Interpreter 여러가지 테스트

## 자료

- `train.csv`: <https://www.kaggle.com/hesh97/titanicdataset-traincsv/data> - kaggle의 Titanic 데이터셋
- `netflix.csv`: <https://www.kaggle.com/datasets/yaminh/netflix-dataset-for-analysis?select=netflix.csv> - kaggle의 Netflix 데이터셋

## `main_assistant.py`

Assistant에 file을 포함한 Code Interpreter를 사용

질문:

- 성별 생존율을 말해줘
- 성별 생존자 수를 말해 줘

## `main_thread.py`

Thread에 file을 포함한 Code Interpreter를 사용

질문:

- 성별 생존율을 말해줘
- 성별 생존자 수를 말해 줘

## `main_message.py`

Message에 file을 포함한 Code Interpreter를 사용

질문:

- 성별 생존율을 말해줘
- 성별 생존자 수를 말해 줘

결과:

- Message에 file을 한 번 attach 하면, 다음 질의 때 파일을 attach하지 않아도 파일 내용을 참조합니다.

## `main_image.py`

답변에 이미지를 포함 한 경우 처리

- 성별 생존율을 말해줘
- 성별 생존율을 막대 그래프로 보여줘

## `main_csv.py`

답변에 csv를 포함 한 경우 처리

- 성별 생존율을 말해줘
- 성별 생존율을 csv 파일로 작성해줘
- 연령대별 생존자수를 csv 파일로 작성해줘