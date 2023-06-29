from components.audio_downloader import download_audio
from components.whisper_model import transcribe

#Setup
youtube_link = "https://www.youtube.com/watch?v=4y8688WOXis&list=WL&index=2&t=15s"
output_dir = "./transcript"

#---Downloading---
file = download_audio(youtube_link,output_dir)

print("[success] audio file exported: "+ file)

#---Transcribing---
transcribe(file)

print("[success] Output saved to transcript/output.txt")

#---Summarizing--