from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import urllib.request

client = OpenAI()

images = client.images.generate(
  model="dall-e-3",
  prompt="A cute baby sea otter",
  n=1,
  size="1024x1024"
)

urllib.request.urlretrieve(images.data[0].url, "./baby_sea_otter.png")
print(images.data[0].url)