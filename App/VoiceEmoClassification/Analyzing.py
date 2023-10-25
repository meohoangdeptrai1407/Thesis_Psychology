import numpy as np
import librosa
from keras.models import load_model
import joblib
import os


model_path = os.path.join(os.path.dirname(__file__), "emotion_model.h5")
model = load_model(model_path)
label_encoder_path = os.path.join(os.path.dirname(__file__), "label_encoder.pkl")
label_encoder = joblib.load(label_encoder_path)

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
new_audio = os.path.join(os.path.dirname(__file__), "audio_output.wav")


def analyzing():
    new_audio_mfcc = extract_mfcc(new_audio, num_mfcc=40)
    if new_audio_mfcc is not None:
        new_audio_mfcc = np.mean(new_audio_mfcc, axis=0)  # Take the mean across the channel axis
        new_audio_mfcc = np.expand_dims(new_audio_mfcc, axis=0)
        prediction = model.predict(new_audio_mfcc)
        emotion_label = label_encoder.inverse_transform(np.argmax(prediction, axis=1))[0]
        percentage = np.max(prediction) * 100
        file_name = os.path.basename(new_audio)

        result = f'file name : {file_name}\n'
        if emotion_label == "ps":
            result += f"Predicted emotion: pleasant-surprised\n"
        else:
            result += f"Predicted emotion: {emotion_label}\n"
        result += f"Percentage detection: {percentage}%\n"
        print(f"result: {result}")
        return result

