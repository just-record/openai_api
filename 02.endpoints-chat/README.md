# OpenAI Endpoints Chat

API: <https://platform.openai.com/docs/api-reference/chat>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## Chat - 답변 생성

`chat_basic.py`: 텍스트를 음성으로 변환하기

결과:

```text
Hello! How can I assist you today?
```

## Chat - 이전 대화 내용 알려 주기

`chat_previous.py`: 인공지능은 조금 전에 대화한 내용을 기억하지 못합니다. 이전의 대화 내용을 알려 주어야 합니다.

결과:

```text
Your name is Hong Gildong
```

## Chat - system role

`chat_system.py`: system role을 사용하여 대화의 지침을 설정할 수 있습니다.

결과: 사용자의 prompt에 영어로 번역 해 달라는 지시가 없어도 사용자의 질의(chat)를 영어로 번역합니다.

```text
Hello. Nice to meet you.
```

## Chat - 여러 개의 답변

`chat_multiple.py`: 여러 개의 답변을 생성할 수 있습니다.

결과:

```text
답변 개수: 3
답변 1: 내 강점은 다양한 주제에 관한 정보를 신속하고 정확하게 제공하는 것입니다.
답변 2: 질문에 최대한 정확하고 빠르게 답변해 드립니다.
답변 3: 사용자를 도와주는 것!
```

## Chat - Token 사용량

`chat_token.py`: 사용한 토큰의 양을 확인할 수 있습니다.

결과:

```text
{'completion_tokens': 60, 'prompt_tokens': 38, 'total_tokens': 98}
```

- `completion_tokens`: 답변 생성(output)에 사용한 토큰의 양
- `prompt_tokens`: 질문(input)에 사용한 토큰의 양
- `total_tokens`: 사용한 총 토큰의 양

## Chat - JSON 모드

`chat_json.py`: 답변을 JSON 형식으로 출력할 수 있습니다.

'gpt-3.5-turbo-0125', 'gpt-4-turbo-preview' 모델이 사용 가능합니다. 다른 모델들 중 'gpt-3.5-turbo-0613'는 사용이 불가능 한 걸 확인했습니다.

결과:

```json
{
  "winner": "Los Angeles Dodgers",
  "year": 2020
}
```

## Chat - Image 질의 (URL)

`chat_image_url.py`: 인터넷에 있는 이미지에 관련된 질문을 할 수 있습니다.

![이미지 URL](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg)

결과: Url 경로의 이미지를 설명 해 줍니다.

```text
이 이미지는 푸른 하늘 아래, 들판을 가로질러 나 있는 나무 데크 길을 보여줍니다. 이 길은 풍부한 녹색 풀밭을 관통하고 있으며, 주변에는 수풀과 나무들이 보입니다. 맑은 날씨와 자연의 풍경이 조화롭게 어우러져 평화로운 분위기를 연출하고 있습니다.
```

## Chat - Image 질의 (Base64)

`chat_image_base64.py`: 이미지를 Base64로 인코딩하여 질의할 수 있습니다. 이미지는 `otter.png` 파일을 사용합니다.

![수달 이미지](otter.png)

결과:

```text
이 이미지에는 물에서 헤엄치고 있는 아주 귀여운 수달 한 마리가 나와 있습니다. 수달은 명랑한 표정을 짓고 있으며, 물결과 햇빛이 반짝이는 배경과 함께 매우 평화로워 보입니다.
```

`chat_image_base64_requests.py`: 위와 동일한 예제를 Python의 requests를 사용하여 구현 하기

requests 설치:

```bash
pip install requests
```

결과:

```text
이 이미지에는 물속에서 수영하고 있는 귀여운 수달 한 마리가 있습니다. 푸른 물결 사이로 반짝이는 눈과 부드러운 털이 특징적인 이 수달은 깜찍한 표정을 짓고 있습니다. 배경에는 맑은 하늘과 햇빛이 반사된 물결이 보입니다.
```

## Chat - 다중 Image 질의 (File)

`chat_image_files.py`: 여러 개의 이미지를 질의합니다. 하나는 `otter.png` 파일을 업로드 하고 다른 하나는 위에서 연습 한 인터넷 상의 이미지 URL을 사용합니다.

결과:

```text
첫 번째 이미지는 물 위에 떠 있는 귀여운 수달의 일러스트레이션을 보여줍니다. 수달의 눈이 밝고 표정이 친근감 있게 묘사되어 있습니다.

두 번째 이미지는 넓은 초록색 잔디밭과 하늘을 배경으로 한 목재 데크 길이 있는 풍경 사진입니다. 이 길은 자연 속을 산책하거나 탐험하는 데 이상적인 경치를 제공하고 있습니다.

두 이미지 사이의 가장 큰 차이점은 첫 번째는 애니메이션으로 제작된 동물의 초상화이고, 두 번째는 실제 자연 풍경의 사진이라는 점입니다. 첫 번째 이미지는 예술적인 요소가 강조되어 있으며, 두 번째 이미지는  
자연 그대로의 아름다움을 보여 줍니다.
```

## Chat - Streaming

`chat_streaming.py`: 답변을 스트리밍으로 출력합니다.

결과: Streaming으로 출력

```text
Of course! I'll be happy to provide a detaile...
```

## Chat - Functions

`chat_functions.py`: tools를 사용하여 Functions를 호출 할 수 있는 형태를 생성합니다.

- `def get_current_weather(location: str, unit: str = "celsius")`: 함수를 선언합니다.
- `tools`: AI에서 생성 할 함수를 정의합니다.
- API response를 사용하여 함수(get_current_weather)를 호출합니다.

결과:

```text
The current weather in Boston, MA is 37 degrees celsius.
```

## Chat - Logprobs

`chat_logprobs.py`: logprobs를 사용하여 각 토큰의 확률을 출력합니다.

결과:

```text
Hello! How can I assist you today?
--------------------
1 - token: Hello, logprob: -0.31725305
    1 - token: Hello, logprob: -0.31725305
    2 - token: Hi, logprob: -1.3190403

2 - token: !, logprob: -0.02380986
    1 - token: !, logprob: -0.02380986
    2 - token:  there, logprob: -3.787621

3 - token:  How, logprob: -5.4669687e-05
    1 - token:  How, logprob: -5.4669687e-05
    2 - token: <|end|>, logprob: -10.953937

4 - token:  can, logprob: -0.015801601
    1 - token:  can, logprob: -0.015801601
    2 - token:  may, logprob: -4.161023

5 - token:  I, logprob: -3.7697225e-06
    1 - token:  I, logprob: -3.7697225e-06
    2 - token:  assist, logprob: -13.596657

6 - token:  assist, logprob: -0.04571125
    1 - token:  assist, logprob: -0.04571125
    2 - token:  help, logprob: -3.1089056

7 - token:  you, logprob: -5.4385737e-06
    1 - token:  you, logprob: -5.4385737e-06
    2 - token:  today, logprob: -12.807695

8 - token:  today, logprob: -0.0040071653
    1 - token:  today, logprob: -0.0040071653
    2 - token: ?, logprob: -5.5247097

9 - token: ?, logprob: -0.0008108172
    1 - token: ?, logprob: -0.0008108172
    2 - token: ?
, logprob: -7.184561
```
