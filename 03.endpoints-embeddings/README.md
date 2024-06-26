# OpenAI Endpoints Embedding

API: <https://platform.openai.com/docs/api-reference/embeddings>

각 코드의 실행은 해당 디렉토리에서 다음과 같이 실행합니다.

```bash
python {실행하고자 하는 파일 이름}
```

## 임베딩(Embedding) 생성

`create_embedding.py`: 임베딩 벡터 생성 하기

결과: 1536차원의 임베딩 벡터를 생성합니다.

```text
Embedding vector의 길이: 1536
Embedding vector - 앞에서 10개 값: [-0.014749587, -0.019521875, -0.0037461228, -0.020424407, -0.022044016, 0.015862295, -0.025419237, 0.008067146, -0.008091873, 0.004073754]
```

## 임베딩 벡터의 차원

`embedding_dimension.py`: 동일한 임베딩 모델은 동일한 벡터 차원을 생성 하는지 확인합니다.

결과: 3개의 다른 문장의 차원은 1,536개로 동일하였고 벡테 값은 모두 달랐습니다.

```text
0번 문장의 Embedding vector의 길이: 1536
0번 문장의 Embedding vector - 앞에서 10개 값: [-0.014749587, -0.019521875, -0.0037461228, -0.020424407, -0.022044016, 0.015862295, -0.025419237, 0.008067146, -0.008091873, 0.004073754]
1번 문장의 Embedding vector의 길이: 1536
1번 문장의 Embedding vector - 앞에서 10개 값: [-0.0046398193, -0.0037137263, 0.009298347, -0.02644198, 0.0038696341, 0.01648882, 0.0042562857, 0.009909506, -0.013807204, 0.011512239]
2번 문장의 Embedding vector의 길이: 1536
2번 문장의 Embedding vector - 앞에서 10개 값: [-0.009437798, -0.005597814, 0.011033466, -0.03842578, -0.010060498, 0.015411826, -0.0073621306, -0.0006109433, 0.0018324245, 0.0031621486]
```

## 문장(임베딩 벡터)의 유사도 확인

`embedding_similarity.py`: 두 문장의 유사도를 계산합니다.

'코사인 유사도(Cosine Similarity)'를 사용하여 두 문장의 유사도를 계산합니다.

- 첫번째 문장: 나는 학교에 다니는 학생이다.
- 두번째 문장: 나는 학생을 가르치는 선생님다.
- 세번째 문장: 오늘 날씨가 좋아서 나들이를 가고 싶다.

첫번째 문장 : 두번째 문장 | 첫번째 문장 : 세번째 문장

결과:

```text
첫번째 문장과 두번째 문장의 거리: 0.07935289192352712
첫번째 문장과 세번째 문장의 거리: 0.1924438784161303
```
