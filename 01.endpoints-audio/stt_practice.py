from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

openai = OpenAI()

audio_file_path = "./speech.mp3"
audio_file = open(audio_file_path, "rb")
transcript = openai.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcript.text)

