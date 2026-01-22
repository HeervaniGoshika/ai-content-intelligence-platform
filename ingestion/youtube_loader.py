import tempfile
import os
from faster_whisper import WhisperModel
import subprocess

model = WhisperModel("base", device="cpu")

def load_youtube(url):
    temp_dir = tempfile.mkdtemp()
    audio_path = os.path.join(temp_dir, "audio.mp3")

    # Download audio using yt-dlp
    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "-o", audio_path,
        url
    ]
    subprocess.run(cmd, check=True)

    # Transcribe
    segments, _ = model.transcribe(audio_path)
    text = ""
    for seg in segments:
        text += seg.text + " "

    return text.strip()
