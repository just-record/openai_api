# OpenAI Endpoints Moderations

API: <https://platform.openai.com/docs/api-reference/moderations>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## Moderations 생성

`create_moderation.py`: Moderations를 생성 하여 텍스트가 잠재적으로 유해한지 확인합니다.

결과:

```text
True
-----------
harassment:  True
harassment_threatening:  True
hate:  False
hate_threatening:  False
self_harm:  False
self_harm_instructions:  False
self_harm_intent:  False
sexual:  False
sexual_minors:  False
violence:  True
violence_graphic:  False
self-harm:  False
sexual/minors:  False
hate/threatening:  False
violence/graphic:  False
self-harm/intent:  False
self-harm/instructions:  False
harassment/threatening:  True
-----------
harassment:  0.5278584957122803
harassment_threatening:  0.5712487697601318
hate:  0.2324090600013733
hate_threatening:  0.024183575063943863
self_harm:  2.3696395601291442e-06
self_harm_instructions:  1.132860139030356e-09
self_harm_intent:  1.7161115692942985e-06
sexual:  1.205232911161147e-05
sexual_minors:  7.506431387582779e-08
violence:  0.997192919254303
violence_graphic:  3.399916022317484e-05
self-harm:  2.3696395601291442e-06
sexual/minors:  7.506431387582779e-08
hate/threatening:  0.024183575063943863
violence/graphic:  3.399916022317484e-05
self-harm/intent:  1.7161115692942985e-06
self-harm/instructions:  1.132860139030356e-09
harassment/threatening:  0.5712487697601318
```
