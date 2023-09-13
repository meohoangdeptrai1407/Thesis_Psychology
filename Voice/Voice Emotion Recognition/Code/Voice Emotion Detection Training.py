import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import librosa
import librosa.display
from IPython.display import Audio
import warnings
from pydub import AudioSegment
from pydub.playback import play
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout



#Training Info

BATCH = 32
EPOCH = 500

warnings.filterwarnings('ignore')

DIR = r"../DataSet"  # Use raw string literal (r"") to avoid escape characters

paths = []
labels = []
for dirname, _, filenames in os.walk(DIR):
    for filename in filenames:
        paths.append(os.path.join(dirname, filename))

        label = filename.split('_')[-1]
        label = label.split('.')[0]
        labels.append(label.lower())

print('Dataset is loaded')

print(paths[:5])
print(labels[:5])

df = pd.DataFrame()
df['speech'] = paths
df['label'] = labels

print(df.head())

label_counts = df['label'].value_counts()

print(label_counts)

plt.figure(figsize=(8, 6))
sns.barplot(x=label_counts.index, y=label_counts.values)
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Distribution of Emotions')
plt.savefig('Bar Figure.png')
plt.show()


def waveplot(data, sr, emotion):
    plt.figure(figsize=(20, 8))
    plt.title(emotion, size=30)
    librosa.display.waveshow(data, sr=sr)
    plt.savefig(f'{emotion} waveplot.png')
    plt.show()


def spectrogram(data, sr, emotion):
    x = librosa.stft(data)
    xdb = librosa.amplitude_to_db(abs(x))
    plt.figure(figsize=(20, 8))
    plt.title(emotion, size=30)
    librosa.display.specshow(xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.savefig(f'{emotion} spectrogram.png')
    plt.show()


emotion = 'angry'

path = np.array(df['speech'][df['label'] == emotion])[0]

print(f'path = {path}')

data, sampling_rate = librosa.load(path)

print(f'data shape: {data.shape}')
print(f'sampling rate: {sampling_rate}')

waveplot(data, sampling_rate, emotion)
spectrogram(data, sampling_rate, emotion)

print(f'path = {path}')

# Play the audio file using pydub
# audio = AudioSegment.from_file(path)
# play(audio)


def extract_mfcc(filename):
    y, sr = librosa.load(filename, duration=3, offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc

print(f'speech array')
print(extract_mfcc(df['speech'][0]))

# Ensure the dataset includes all the emotions
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'ps', 'sad']
df = df[df['label'].isin(emotions)]

X_mfcc = df['speech'].apply(lambda x: extract_mfcc(x))

## Label encoding
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(df['label'])

X = [x for x in X_mfcc]
X = np.array(X)
X = np.expand_dims(X, -1)

y = to_categorical(encoded_labels)


# Modify the model architecture and the number of output neurons
num_emotions = len(emotions)
model = Sequential([
    LSTM(123, return_sequences=False, input_shape=(40, 1)),
    Dense(64, activation="relu"),
    Dropout(0.8),
    Dense(32, activation="relu"),
    Dropout(0.2),
    Dense(7, activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Train the model
history = model.fit(X, y, validation_split=0.2, epochs=EPOCH, batch_size=BATCH, shuffle=True)


# Get the final accuracy
accuracy = history.history['accuracy'][-1] * 100

# Save the model accuracy to info.txt
with open('info.txt', 'w') as file:
    file.write(f'accuracy: {accuracy:.2f}%')

epochs = EPOCH
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
# plt.plot(epochs, acc, label='train accuracy')
# plt.plot(epochs, val_acc, label='val accuracy')
# plt.xlabel('epochs')
# plt.ylabel('accuracy')
# plt.legend()
# plt.show()




loss =  history.history['loss']
val_loss = history.history['val_loss']
# plt.plot(epochs, loss, label='train loss')
# plt.plot(epochs, val_loss, label='val loss')
# plt.xlabel('epochs')
# plt.ylabel(loss)
# plt.legend()
# plt.show()

# Save the trained model
model.save("emotion_model.h5")

# Save the label encoder
import joblib
joblib.dump(label_encoder, "label_encoder.pkl")

# # Perform inference on new audio samples
# new_audio_path = f"D:\\Emotion Image\\Neutral\\raw\\y2mate.com - Oh my God Inhuman Reactions Sound effect_320kbps.mp3"  # Replace with the path to your new audio sample
# new_audio_mfcc = extract_mfcc(new_audio_path)
# new_audio_mfcc = np.expand_dims(new_audio_mfcc, axis=0)
# prediction = model.predict(new_audio_mfcc)
# emotion_label = label_encoder.inverse_transform(np.argmax(prediction, axis=1))[0]
#
# print("Predicted emotion:", emotion_label)
