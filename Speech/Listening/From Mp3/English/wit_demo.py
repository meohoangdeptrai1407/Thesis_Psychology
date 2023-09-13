import speech_recognition as sr
from pydub import AudioSegment

# Load audio
audio_file = "oh-my-god-inhuman-reactions-sound-effect-128-ytshorts.savetube.me.mp3"
audio = AudioSegment.from_file(audio_file)

# Get raw audio data
raw_audio = audio.raw_data
sample_rate = audio.frame_rate
sample_width = audio.sample_width

# Convert to AudioData
audio_data = sr.AudioData(raw_audio, sample_rate, sample_width)

# Initialize recognizer
r = sr.Recognizer()

WIT_AI_KEY = "N4M3MLG3BJZIP4547W432WWL6HWCFSZL"

try:
    # Transcribe audio using Wit.ai
    print("Transcribing via Wit.ai...")
    text = r.recognize_wit(audio_data, key=WIT_AI_KEY)
    print(text)

except Exception as e:
    print(e)

