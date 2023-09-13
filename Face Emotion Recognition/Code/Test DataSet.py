import cv2
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('new_emotion_model.h5')

# Define the emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


# Function to preprocess the image for prediction
def preprocess_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (48, 48))
    img = img.reshape(1, 48, 48, 1)
    img = img.astype('float32')
    img /= 255.0
    return img


# Function to predict the emotion from an image
def predict_emotion(image):
    img = preprocess_image(image)
    emotion_prediction = model.predict(img)
    emotion_scores = emotion_prediction[0] * 100
    return emotion_scores


# Function to detect emotions in an image using bounding boxes
def detect_emotions(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_img = image[y:y + h, x:x + w]
        emotion_scores = predict_emotion(face_img)
        dominant_emotion = np.argmax(emotion_scores)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'{emotion_labels[dominant_emotion]}: {emotion_scores[dominant_emotion]:.2f}',
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        sorted_emotion_indices = np.argsort(emotion_scores)[::-1]

        for index in sorted_emotion_indices:
            print(f'{emotion_labels[index]}: {emotion_scores[index]:.2f}')

    cv2.imshow('Emotion Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = 'D:\\Emotion Image\\Neutral\\raw\\DMUbjq2UjJcG3umGv3Qjjd.jpeg'
detect_emotions(image_path)