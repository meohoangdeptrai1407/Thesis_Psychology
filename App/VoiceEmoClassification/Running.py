from pydub import AudioSegment
from pydub.playback import play
import os
def play_audio(audio_filename):
    audio = AudioSegment.from_file(audio_filename)
    play(audio)

def run():
# Example usage
    path = "audio_output.wav"
    play_audio_path = os.path.join(os.path.dirname(__file__), path)
    play_audio(play_audio_path)
    return path

