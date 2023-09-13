import speech_recognition as sr
from pydub import AudioSegment

# Load the audio file
audio_file = "y2mate.com - Phan Sơn  Bố nhịn mày lâu lắm rồi đấy nhớ_320kbps.mp3"

# Convert MP3 to WAV using pydub
audio = AudioSegment.from_mp3(audio_file)
audio.export("output.wav", format="wav")

# Initialize the recognizer
r = sr.Recognizer()

# Load the WAV file
with sr.AudioFile("output.wav") as source:
    # Read the entire audio file
    audio = r.record(source)

# Use the recognizer to convert audio to text using Google Speech Recognition
try:
    text = r.recognize_google(audio, language="vi-VN")
    print("Transcription:")
    print(text)
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from the speech recognition service: {0}".format(e))