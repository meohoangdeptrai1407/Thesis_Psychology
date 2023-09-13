import speech_recognition as sr

robot_ear = sr.Recognizer()
# Set the energy threshold (adjust as needed)
robot_ear.energy_threshold = 8000

STOPWORD = ["dừng lại", "dừng"]
while True:
    with sr.Microphone() as mic:
        print("Robot: Tôi đang lắng nghe...")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio, language="vi-VN")
        print(f"Bạn: {you.capitalize()}")
    except sr.UnknownValueError:
        print("Robot: Xin lỗi, tôi không hiểu bạn nói gì.")
    except sr.RequestError:
        print("Robot: Xin lỗi, có lỗi xảy ra trong việc xử lý giọng nói.")

    if you.lower() in STOPWORD:
        print("Robot: Dừng chương trình.")
        break