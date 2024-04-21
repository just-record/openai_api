from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

client = OpenAI()

content = client.files.content("file-uoBfFNii72tm9cueSCK2i69J")

# file = client.files.retrieve("file-uoBfFNii72tm9cueSCK2i69J")
# print(file.filename)
file_path = "./image.png"
content.write_to_file(file_path)
# print(content.content.decode('utf-8')) # bytes to string