import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")



engine.setProperty("voice", voices[1].id) # Giọng đọc của anh An
engine.say("Xin chào các bạn")
engine.runAndWait()

