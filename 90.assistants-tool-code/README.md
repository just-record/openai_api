# Tool('code_interpreter')을 사용 하여 데이터 분석 하기

API: <https://platform.openai.com/docs/api-reference/assistants>

가이드: <https://platform.openai.com/docs/assistants/overview/agents>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

<!-- ## 파일 업로드

먼저 분석할 csv 파일을 업로드 합니다. 업로드 할 파일은 다음과 같습니다.

`train.csv`: 자료출처 - <https://www.kaggle.com/hesh97/titanicdataset-traincsv/data>, kaggle의 Titanic 훈련용 데이터셋

- 신규 파일 업로드
  - `06.endpoints-file/upload_file.py`: 파일 업로드
- 기존 업로드 된 파일 검색
  - `06.endpoints-file/list_files.py`: 업로드 된 파일 목록을 조회
  - `06.endpoints-file/retrieve_file.py`: 파일 ID로 특정 파일 검색 -->

## 자료 출처

- `train.csv`(최초 등록): <https://www.kaggle.com/hesh97/titanicdataset-traincsv/data> - kaggle의 Titanic 훈련용 데이터셋
- `netflix.csv`(변경할 파일): <https://www.kaggle.com/datasets/yaminh/netflix-dataset-for-analysis?select=netflix.csv> - kaggle의 Netflix 데이터셋

## 업로드한 파일 내용을 질의 하기

`main.py`: 파일을 업로드 하고 Assistant를 생성하여 질의 하기. Assistant를 생성할 때, file_ids를 설정하여 Assistant가 사용할 파일을 지정합니다. 나머지는 동일합니다.

질문:

- 몇 개의 항목과 몇 건의 데이터가 있는지 알려줘.
- 생존율을 성별로 말해줘.

`/q`를 입력하면 대화를 종료합니다.

결과: 파일의 내용을 잘 분석하여 답변 합니다.

## 업로드 된 파일을 질의 하다가 중간에 다른 파일로 변경 하기

`main_modify_file.py`: 질의 하다가 중간에 file을 변경 하기. 최초 Assistant 생성 시에 file을 지정하고 질의를 하다가 중간에 다른 file로 변경 하여 질의 합니다.

### 변경할 파일

`/f`를 입력하면 Assistants의 file(분석 파일)을 위의 파일로 변경합니다.

결과: **변경이 안 되는 듯 합니다**

** Assistant가 파일을 한 번 로드하면 다른 file로 변경 하여도 적용이 되지 않는 듯 합니다. 최초 생성 시의 file을 로드 하지 않으면(질의를 하지 않으면) 두번 째 파일을 변경 하면 잘 변경이 됩니다.

## 업로드 된 파일을 질의 하다가 중간에 다른 파일로 변경 하기 - Thread를 다시 생성 하기

`main_modify_file_thread.py`: Assistant의 파일을 변경하고 Thread를 다시 생성 하기. Assistant의 파일을 변경하고 Thread를 다시 생성하여 Assistant가 새로운 Thread를 사용하도록 합니다.

결과: Thread를 새로 생성해서 Run을 하니 파일이 **변경이 됩니다.** 답변도 잘 합니다.
