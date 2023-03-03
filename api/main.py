from fastapi import FastAPI, File, UploadFile
import openai
import os

app = FastAPI()

#Configure the API key
openai.api_key = os.getenv("OPENAI_KEY")


@app.post("/process-audio")
async def process_audio(file: UploadFile = File(...)):
    # Save file into the audios folder

    file_location = f"./audios/{file.filename}"
    with open(file_location, "wb+") as audio:
        audio.write(file.file.read())
    
    # Open the file and transcribe it
    audio_file = open(f"./audios/{file.filename}", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    
    # Delete the file
    os.remove(file_location)

    return {"text": transcript}
