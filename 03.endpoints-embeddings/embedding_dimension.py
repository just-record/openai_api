from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


model = "text-embedding-ada-002"
sentences = [
    '나는 학교에 다니는 학생이다.',
    '나는 학생을 가르치는 선생님다.',
    '오늘 날씨가 좋아서 나들이를 가고 싶다.'
]


client = OpenAI()


for i, sentence in enumerate(sentences):
    embedding = client.embeddings.create(
    model=model,
    input=sentence,
    encoding_format="float"
    )

    embedding_vector = embedding.data[0].embedding

    print(f'{i}번 문장의 Embedding vector의 길이: {len(embedding_vector)}')
    print(f'{i}번 문장의 Embedding vector - 앞에서 10개 값: {embedding_vector[:10]}')
