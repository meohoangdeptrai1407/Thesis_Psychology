import tkinter as tk
import Main
from LLMPsychology import LLMPsychology

def process():
    print(f"The result:")
    LLMPsychology.run()
def navigate_to_Main():
    root.destroy()
    Main.create_a_window()

def create_LLMPsychology_window():
    global root
    root = tk.Tk()
    HEIGHT = 800
    WIDTH = 800
    root.geometry(f"{HEIGHT}x{WIDTH}")
    root.title("LLM Psychology")
    # Load the modified image as a PhotoImage
    bg_image = tk.PhotoImage(file="background.png")

    # Create a Label widget to display the image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    button = tk.Button(root, text="Run", command=process, bg="purple", fg="white")
    button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    button = tk.Button(root, text="Main", command=navigate_to_Main, bg="purple", fg="white")
    button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Center the window on the screen.
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()