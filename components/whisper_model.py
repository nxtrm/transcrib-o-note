import whisper


def transcribe(file):
    print("[transctibe] Starting transcription process...")

    #load the model
    model = whisper.load_model("base")
    result = model.transcribe(file)
    print("[transctibe] Decoding audio...")

    # Write the model output to the file
    try:
        with open("./transcript/output.txt", "w") as file:
            
            file.truncate(0)
            file.write(str(result))
    except:
        with open("./transcript/output.txt", "w") as file:
            file.write(str(result))

    