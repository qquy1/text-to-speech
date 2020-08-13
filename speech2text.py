import pyttsx3
import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
import time
# function for speech recognition
def get():
    global text
    text = None
    r = sr.Recognizer()
    # text_box.insert(tk.INSERT, "Say something...\n")

    with sr.Microphone() as source:
        # print('Say something...')
        audio = r.listen(source)
        # print('Done!')
        # text_box.insert(tk.INSERT, "Done! \n")
    try:
        text = r.recognize_google(audio)
        # print('You said :' + text)
        text_box.insert(tk.INSERT, text+"\n")
    except Exception as e:
        print(e)

# save function
def save():
    fn = filedialog.asksaveasfilename(defaultextension=".txt").replace('/', '\\')
    with open(fn, 'w') as file:
        file.write(text_box.get('1.0', tk.END))
        file.close()

# clear function
def clear():
    text_box.delete('1.0', tk.END)

root = tk.Tk()
root.title('Speech Recognition')
# row 0
top = tk.Frame(root)
bot = tk.Frame(root)
top.pack(side=tk.TOP)
bot.pack(side=tk.BOTTOM)
# row 1
# begin button
button_begin = tk.Button(root, text="Begin", command=get)
button_begin.pack(in_=top, side=tk.LEFT, expand=True)

# save button
button_save = tk.Button(root, text="Save", command=save)
button_save.pack(in_=top, side=tk.LEFT, expand=True)

# clear button
button_clear = tk.Button(root, text="Clear", command=clear)
button_clear.pack(in_=top, side=tk.LEFT, expand=True)
# row 2
you_said = tk.Label(root, text="You said: ")
you_said.pack(in_=bot)
# row 3
text_box = tk.Text(root)
text_box.pack(in_=bot)
# r
root.mainloop()