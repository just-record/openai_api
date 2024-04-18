from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

audio_file_path = "./speech.mp3"
audio_file = open(audio_file_path, "rb")

transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcript.text)

