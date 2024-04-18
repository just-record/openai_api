from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

speech_file_path = "./speech.mp3"

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy", # "echo", "fable", "onyx", "nova", "shimmer"
  input="안녕하세요! 반갑습니다."
)

response.write_to_file(speech_file_path)