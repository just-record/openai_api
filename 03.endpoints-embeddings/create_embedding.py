from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

embedding = client.embeddings.create(
  model="text-embedding-ada-002", # Embedding 모델 이름
  input="나는 학교에 다니는 학생이다.",
  encoding_format="float"
)

embedding_vector = embedding.data[0].embedding

print(f'Embedding vector의 길이: {len(embedding_vector)}')
print(f'Embedding vector - 앞에서 10개 값: {embedding_vector[:10]}')
