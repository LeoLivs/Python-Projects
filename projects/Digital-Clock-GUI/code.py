from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(100, time)


label = Label(root, font=("Times New Roman", 80), background="pink", foreground="blue")
label.pack(anchor="center")
time()

mainloop()
