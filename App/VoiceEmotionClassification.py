import tkinter as tk
import Main
from VoiceEmoClassification import Running, Analyzing, Recording
import os

def navigate_to_Main():
    root.destroy()
    Main.create_a_window()

def running():
    print("Running the audio")
    Running.run()

def recording():
    print("Recording the audio")

    # Clear the existing text in the recording_text_widget
    recording_text_widget.config(state=tk.NORMAL)  # Enable the widget for editing
    recording_text_widget.delete('1.0', tk.END)  # Clear previous text
    recording_text_widget.config(state=tk.DISABLED)  # Disable editing

    # Display "Start Recording" immediately
    start_recording = "Start Recording"
    start_recording_widget.config(state=tk.NORMAL)  # Enable the widget for editing
    start_recording_widget.delete('1.0', tk.END)  # Clear previous text
    start_recording_widget.insert(tk.END, start_recording)  # Insert the new result
    start_recording_widget.config(state=tk.DISABLED)  # Disable editing

    # Use after to update the recording_text_widget after a delay
    root.after(100, update_recording_text)

def update_recording_text():
    recording_result = Recording.speech_to_text_and_save()

    # Update the text widget with the result
    recording_text_widget.config(state=tk.NORMAL)  # Enable the widget for editing
    recording_text_widget.insert(tk.END, recording_result)  # Insert the new result
    recording_text_widget.config(state=tk.DISABLED)  # Disable editing

def analyzing():
    print("Analyzing the audio")

    # Clear the existing text in the analyze_text_widget
    analyze_text_widget.config(state=tk.NORMAL)  # Enable the widget for editing
    analyze_text_widget.delete('1.0', tk.END)  # Clear previous text
    analyze_text_widget.config(state=tk.DISABLED)  # Disable editing

    # Perform the analysis and get the results
    result_text = Analyzing.analyzing()

    # Use after to update the analyze_text_widget after a delay
    root.after(100, update_analyze_text, result_text)

def update_analyze_text(result_text):
    # Update the text widget with the result
    analyze_text_widget.config(state=tk.NORMAL)  # Enable the widget for editing
    analyze_text_widget.insert(tk.END, result_text)  # Insert the new result
    analyze_text_widget.config(state=tk.DISABLED)  # Disable editing


def create_VoiceEmotionClassification_window():
    global root, analyze_text_widget, recording_text_widget, start_recording_widget
    root = tk.Tk()
    HEIGHT = 800
    WIDTH = 800
    root.geometry(f"{HEIGHT}x{WIDTH}")
    root.title("Voice Emotion Classification")

    # Load the modified image as a PhotoImage
    bg_image = tk.PhotoImage(file="background.png")

    # Create a Label widget to display the image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    button = tk.Button(root, text="Recording", command=recording, bg="purple", fg="white")
    button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    start_recording_widget = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, height=2)  # Adjust the height as needed
    start_recording_widget.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    recording_text_widget = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, height=2)  # Adjust the height as needed
    recording_text_widget.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    button = tk.Button(root, text="Running", command=running, bg="purple", fg="white")
    button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    button = tk.Button(root, text="Analyzing", command=analyzing, bg="purple", fg="white")
    button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    analyze_text_widget = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, height=4)  # Adjust the height as needed
    analyze_text_widget.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    button = tk.Button(root, text="Main", command=navigate_to_Main, bg="purple", fg="white")
    button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Center the window on the screen.
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()

create_VoiceEmotionClassification_window()
