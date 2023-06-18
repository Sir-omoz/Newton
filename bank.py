from tkinter import *
from tkinter import messagebox
import subprocess


root = Tk()

frame = LabelFrame(root, text="Welcome to Vicco Bank...", padx=60, pady=60)
frame.pack(padx=20, pady=20)

def call_python_file(file_path):
    subprocess.call(["python", file_path])

Button(frame, text="Login", padx=30, pady=10, command=lambda: call_python_file("login.py")).pack()

Button(frame, text="Sign up", padx=30, pady=10, command=lambda: call_python_file("sign_up.py")).pack()


mainloop()
