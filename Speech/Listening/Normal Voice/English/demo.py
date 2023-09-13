import speech_recognition as sr

robot_ear = sr.Recognizer()
# Set the energy threshold (adjust as needed)
robot_ear.energy_threshold = 8000

STOPWORD = ["stop it", "stop"]
while True:
    with sr.Microphone() as mic:
        print("Robot: I'm listening...")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)
        print(f"You: {you.capitalize()}")
    except sr.UnknownValueError:
        print("Robot: Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Robot: Sorry, there was an error processing the speech.")

    if you.lower() in STOPWORD:
        print("Robot: Stopping the program.")
        break