from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import urllib.request

client = OpenAI()

images = client.images.edit(
  image=open("otter.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A cute baby sea otter wearing a beret",
  n=1,
  size="1024x1024"
)

urllib.request.urlretrieve(images.data[0].url, "./otter_edited.png")
print(images.data[0].url)