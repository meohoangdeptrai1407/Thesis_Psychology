import numpy as np
import librosa
from keras.models import load_model
import joblib
import os

# Load the saved model
model = load_model("emotion_model.h5")
label_encoder = joblib.load("label_encoder.pkl")

# Function to extract MFCC features
def extract_mfcc(filename, num_mfcc=40):
    try:
        # Load audio file
        audio, sr = librosa.load(filename)

        # Extract MFCC features
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=num_mfcc)

        # Resize MFCC features if necessary
        if mfcc.shape[1] > num_mfcc:
            mfcc = mfcc[:, :num_mfcc]
        elif mfcc.shape[1] < num_mfcc:
            mfcc = np.pad(mfcc, ((0, 0), (0, num_mfcc - mfcc.shape[1])), mode='constant')

        return mfcc
    except Exception as e:
        print("Error occurred during audio processing:", str(e))
        return None

# Perform inference on new audio samples
new_audio_paths = ["y2mate.com - Oh my God Inhuman Reactions Sound effect_320kbps.mp3",
                   "y2mate.com - Yahoo sound effect_320kbps (1).mp3",
                   "output.mp3",
                   "y2mate.com - HAHAHA GAGO SOUND EFFECTS_320kbps.mp3"]  # Replace with the path to your new audio sample

for new_audio_path in new_audio_paths:
    new_audio_mfcc = extract_mfcc(new_audio_path, num_mfcc=40)
    if new_audio_mfcc is not None:
        new_audio_mfcc = np.mean(new_audio_mfcc, axis=0)  # Take the mean across the channel axis
        new_audio_mfcc = np.expand_dims(new_audio_mfcc, axis=0)
        prediction = model.predict(new_audio_mfcc)
        emotion_label = label_encoder.inverse_transform(np.argmax(prediction, axis=1))[0]
        percentage = np.max(prediction) * 100
        file_name = os.path.basename(new_audio_path)
        print(f'file name : {file_name}')
        print(f"Predicted emotion: {emotion_label}", )
        print(f"Percentage detection: {percentage}%")
