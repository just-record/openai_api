from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import base64

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "otter.png"
base64_image = encode_image(image_path)

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image? Please answer me in Korean."},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)