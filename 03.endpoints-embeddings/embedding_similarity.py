# pip install numpy
from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import numpy as np # type: ignore
from numpy.linalg import norm # type: ignore


def cosine_similarity(a,b):
    return np.dot(a,b) / (norm(a)*norm(b))


model = "text-embedding-ada-002"
sentences = [
    '나는 학교에 다니는 학생이다.',
    '나는 학생을 가르치는 선생님다.',
    '오늘 날씨가 좋아서 나들이를 가고 싶다.'
]
vectors = []


client = OpenAI()


for i, sentence in enumerate(sentences):
    embedding = client.embeddings.create(
    model=model,
    input=sentence,
    encoding_format="float"
    )

    vectors.append(embedding.data[0].embedding)

### 첫 번째 문장을 두번째, 세번째 문장과 각각 코사인 유사도 계산 - 값이 작을 수록 가까운 거리
print(f'첫번째 문장과 두번째 문장의 거리: {1 - cosine_similarity(vectors[0], vectors[1])}')
print(f'첫번째 문장과 세번째 문장의 거리: {1 - cosine_similarity(vectors[0], vectors[2])}')
# '나는 학교에 다니는 학생이다.'와 '나는 학생을 가르치는 선생님다.'가 '오늘 날씨가 좋아서 나들이를 가고 싶다.'보다 더 가까운 거리에 있음을 확인할 수 있습니다.
