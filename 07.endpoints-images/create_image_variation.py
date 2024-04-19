from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import urllib.request

client = OpenAI()

images = client.images.create_variation(
  image=open("otter.png", "rb"),
  n=2, # 생성할 이미지의 개수
  size="1024x1024"
)

for i in range(2):
    urllib.request.urlretrieve(images.data[i].url, f"./baby_sea_otter_{i}.png")
    print(images.data[i].url)