import pyaudio
import wave
import time
import os
def record_audio(filename):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    SILENCE_THRESHOLD = 5000  # Minimum silence duration in milliseconds
    TIMEOUT = 5  # Timeout duration in seconds

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    silent_frames = 0  # Counter to track consecutive silent frames
    start_time = time.time()
    if (TIMEOUT <=1):
        print(f"Recording in {TIMEOUT} second")
    else:
        print(f"Recording in {TIMEOUT} seconds")

    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        # Check if the recorded audio is silent
        is_silent = max(abs(sample) for sample in data) < SILENCE_THRESHOLD

        if is_silent:
            silent_frames += 1
            if silent_frames >= int(RATE / CHUNK * TIMEOUT):
                elapsed_time = time.time() - start_time
                if elapsed_time > TIMEOUT:
                    break
        else:
            silent_frames = 0
            start_time = time.time()

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()
    return TIMEOUT

def speech_to_text_and_save():


    filename = os.path.join(os.path.dirname(__file__), "audio_output.wav")

    TIME = record_audio(filename)
    print("Audio saved as", filename)

    # Perform speech recognition on the recorded audio here
    # and print out the result
    return f"The time recording is {TIME} seconds"

