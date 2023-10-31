import tkinter as tk
import ImageEmotionClassification
import LLM
import VoiceEmotionClassification
from tkinter import PhotoImage
from PIL import Image, ImageTk

def navigate_to_ImageEmotionNavigation():
    print("Navigate to Image Emotion Classification")
    root.destroy()
    ImageEmotionClassification.create_ImageEmotionClassification_window()

def navigate_to_VoiceEmotionNavigation():
    print("Navigate to Voice Emotion Classification")
    root.destroy()
    VoiceEmotionClassification.create_VoiceEmotionClassification_window()

def navigate_to_LLMPsychology():
    print("Navigate to LLM Psychology")
    root.destroy()
    LLM.create_LLMPsychology_window()


def quit_application():
    print("Turn off")
    root.destroy()

def create_a_window():


    global root
    root = tk.Tk()
    HEIGHT = 800
    WIDTH = 1200
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("Main")
    # Load the modified image as a PhotoImage
    bg_image = tk.PhotoImage(file="background.png")

    # Create a Label widget to display the image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)



    button = tk.Button(root, text="ImageEmotionClassification", command=navigate_to_ImageEmotionNavigation, bg="red", fg="white")
    button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    button = tk.Button(root, text="VoiceEmotionClassification", command=navigate_to_VoiceEmotionNavigation, bg="red",
                       fg="white")
    button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    button = tk.Button(root, text="LLMPsychology", command=navigate_to_LLMPsychology, bg="red",
                       fg="white")
    button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    button = tk.Button(root, text="Quit", command=quit_application, bg="red",
                       fg="white")
    button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Center the window on the screen.
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()

if __name__ == "__main__":
    create_a_window()