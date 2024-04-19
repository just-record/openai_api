from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI


client = OpenAI()

file_path = './train.csv'
file = client.files.create(
  file=open(file_path, "rb"),
  # 이 중에서 하나만 가능: 'fine-tune', 'assistants', 'batch', 'user_data', 'responses'
  purpose="assistants"
)

print(file.to_dict())
