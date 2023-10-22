import cv2
from PIL import Image
import numpy as np
import time
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

labelData = ["Sad", "Happy", "Neutral", "Fear", "Anger", "Surprise"]

# Open camera
cap = cv2.VideoCapture(0)

# Set frame width and height (adjust as needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Loop to capture and process frames
while True:
    # Capture frame from video feed
    ret, frame = cap.read()

    # Convert BGR frame to RGB PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Perform emotion analysis using CLIP
    inputs = processor(text=labelData, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    probs_list = probs.tolist()[0]
    values = max(probs_list)
    max_index = probs_list.index(values)
    emotion_label = labelData[max_index]
    confidence = "{:.2%}".format(values)
    print(f"The most emotion is: {emotion_label} with confidence: {confidence}")

    # Display frame with emotion label
    cv2.putText(frame, f"Emotion: {emotion_label} ({confidence})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()