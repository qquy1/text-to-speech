import pyttsx3
import tkinter as tk
def tts():
    engine = pyttsx3.init()
    engine.say(entry.get())
    engine.runAndWait()

root = tk.Tk()
root.title("Text2Speech Machine")
# row 0
frame = tk.Frame(root)
frame.grid(row=0)
# row 1
instruction = tk.Label(root, text="Enter the sentence you would to be read out:")
instruction.grid(row=1)
# row 2
entry = tk.Entry(root, width=50)
entry.grid(row=2)
# row 3
submit = tk.Button(root, text="Submit", command=tts)
submit.grid(row=3)


root.mainloop()

