# OpenAI Endpoints Audio

API: <https://platform.openai.com/docs/api-reference/audio>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## text-to-speech

`tts_practice.py`: 텍스트를 음성으로 변환하기

결과:

`speech.mp3` 파일이 생성됩니다. 이 파일을 재생하면 입력 텍스트가 음성으로 변환된 것을 들을 수 있습니다.

## speech-to-text

`stt_practice.py`: 음성을 텍스트로 변환하기, 앞서 생성한 `speech.mp3` 파일을 사용합니다.

결과:

```text
안녕하세요. 반갑습니다.
```
