from google.cloud import speech_v1p1beta1 as speech

# Create a client
client = speech.SpeechClient()

MP3_FILE = 'oh-my-god-inhuman-reactions-sound-effect-128-ytshorts.savetube.me.mp3'

# Transcribe the MP3 file
with open(MP3_FILE, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=16000,
    language_code='en-US'
)

response = client.recognize(config=config, audio=audio)

# Extract the transcribed text
text = response.results[0].alternatives[0].transcript
print("Transcription:")
print(text)