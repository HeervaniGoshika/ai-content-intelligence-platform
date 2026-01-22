from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu")

def load_audio(file_path):
    #return model.transcribe(file_path)["text"]
    segments, _ = model.transcribe(file_path)
    text = ""
    for seg in segments:
        text += seg.text + " "
    return text