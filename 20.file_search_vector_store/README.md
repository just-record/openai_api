# File Search 여러가지 테스트

## `main.py`

Assistant에만 Vector Store를 등록하고 질의하는 방법을 연습합니다.

질의:

- 허생원은 장돌이를 얼마나 했나?
- 허생원은 왜 옷이 젖었나?

## `main_thread.py`

Assistant와 Thread에 Vector Store를 등록하고 질의하는 방법을 연습합니다.

질의: 1,2 - 모밀꽃 / 3, 4 - 동백꽃

- 허생원은 장돌이를 얼마나 했나?
- 허생원은 왜 옷이 젖었나?
- 닭 싸움을 붙인 건 누구인가?
- 내가 점순이에게 건네준 것은 무엇인가?

결과: Assistant와 Thread에 Vector Store의 내용에 대한 답변을 얻을 수 있습니다.

## `main_thread_message.py`

Assistant와 Thread, Message Vector Store를 등록(Message는 file)하고 질의하는 방법을 연습합니다.

- 첫번째 질의 때 Message에 파일을 attach하고, 관련 질의를 하고 두번째 질의 때 Message에 파일을 attach하지 않고 관련 파일 질의를 합니다.
- 세번째 질의 때 Assistant Vector Store에 등록된 내용을 질의하고, 네번째 질의 때 Thread Vector Store에 등록된 내용을 질의합니다.
- 다섯번째 질의 때 Message에 다른 파일을 attach하고, 관련 질의를 합니다.
- 여섯번째 질의 때 Message에 파일을 attach하지 않고 첫번째 파일의 질의를 합니다.

질의:

- 1 - 광염_소나타(Message 첫번째)
- 2 - 광염_소나타(Message 첫번째)
- 3 - 모밀꽃(Assistant)
- 4 - 동백꽃(Thread)
- 5 - 운수 좋은날(Message 두번째)
- 6 - 광염_소나타(Message 첫번째)
- 7 - 모밀꽃(Assistant)
- 8 - 동백꽃(Thread)
- 9 - 모든 파일에 내용이 없으며 거짓 정보를 질의
- 10 - 모든 파일에 내용이 없으며 일반 상식인 내용을 질의

- 백성수의 다른 이름은 무엇인가?
- 백성수가 작곡한 곡은 무엇인가?
- 허생원은 장돌이를 얼마나 했나?
- 닭 싸움을 붙인 건 누구인가?
- 김첨지의 아내가 먹고 싶어 했던 음식은 무엇인가?
- 백성수의 아버지는 어떤 일을 하셨나?
- 허생원은 왜 옷이 젖었나?
- 내가 점순이에게 건네준 것은 무엇인가?
- 세종대왕이 작곡한 곡은 무엇인가?
- 음악의 아버지는 누구인가?

결과:

- Message에 파일을 한 번 attach 하면, 다음 질의 때 파일을 attach하지 않아도 파일 내용을 참조합니다.
- Message에 파일을 attach 해도 Assistant와 Thread의 Vector Store에 등록된 내용을 질의할 수 있습니다.
- Message에 파일을 attach 하고 다른 파일을 attach 해도 이전의 attach한 파일을 참조합니다.(대체 되지 않습니다.)
- 파일에 내용이 없는 거짓 정보인 경우 잘못 된 정보임을 알려죽고 파일에 내용이 없음도 알려 줍니다.
- 파일에 내용이 없는 일반 상식인 경우 일반 상식을 알려 줍니다.
