from tkinter import *
from tkinter import messagebox

root = Tk()

frame = LabelFrame(root, text="Login...", padx=60, pady=60)
frame.pack(padx=20, pady=20)

def popup():
    messagebox.showinfo("Login", "Account dosen't exist")


root.title("login")

Lbl2 = Label(frame, text="Enter Phone No :")
Lbl2.grid(row=0, column=0)

Lbl3 = Label(frame, text="Password :")
Lbl3.grid(row=1, column=0)

Ent4 = Entry(frame, width=15, borderwidth=5)
Ent4.grid(row=0, column=1)

Ent5 = Entry(frame, width=15, borderwidth=5)
Ent5.grid(row=1, column=1)

btn6 = Button(frame, text="quit", command=root.destroy)
btn6.grid(row=2, column=0)

btn7 = Button(frame, text="Login", command=popup)
btn7.grid(row=2, column=1)


root.mainloop()