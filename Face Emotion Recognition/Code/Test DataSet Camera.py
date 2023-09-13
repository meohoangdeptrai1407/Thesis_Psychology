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


# Function to detect emotions in a video stream using bounding boxes
def detect_emotions():
    cap = cv2.VideoCapture(0)  # Open the default camera (index 0)

    while True:
        ret, frame = cap.read()  # Read a frame from the video stream
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_img = frame[y:y + h, x:x + w]
            emotion_scores = predict_emotion(face_img)
            dominant_emotion = np.argmax(emotion_scores)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'{emotion_labels[dominant_emotion]}: {emotion_scores[dominant_emotion]:.2f}',
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            sorted_emotion_indices = np.argsort(emotion_scores)[::-1]

            # for index in sorted_emotion_indices:
            #     print(f'{emotion_labels[index]}: {emotion_scores[index]:.2f}')

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the video stream
            break

    cap.release()
    cv2.destroyAllWindows()


# Invoke the video stream emotion detection
detect_emotions()