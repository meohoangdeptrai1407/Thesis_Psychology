import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech, default is 200
engine.setProperty("volume", 0.8)  # Volume (0.0 to 1.0), default is 1.0

# Provide the text to be converted to speech
text = "Hello, how are you?"

# Convert text to speech
engine.say(text)

# Play the speech
engine.runAndWait()