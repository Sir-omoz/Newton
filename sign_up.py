from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """
)


root = tk.Tk()

r = IntVar()

def submit():
    #clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    name_entry.delete(0, END)
    name_entry.delete(0, END)


def save_data():
    name = name_entry.get()
    age = age_entry.get()

    # Insert the data into the table
    cursor.execute("INSERT INTO my_table VALUES (:f_name, :l_name, :age_label, :name_label)")
    conn.commit()

def popup():
    messagebox.showinfo("Sign up", "successful!...")

root.title("Sign up")

frame = LabelFrame(root, text="Welcome to Vicco Bank...", padx=60, pady=60)
frame.pack(padx=20, pady=20)


f_name = tk.Label(frame, text="First Name :")
f_name.grid(row=0, column=0)
f_name = tk.Entry(frame)
f_name.grid(row=0, column=1)

l_name = tk.Label(frame, text="Last Name:")
l_name.grid(row=1, column=0)
l_name = tk.Entry(frame)
l_name.grid(row=1, column=1)

age_label = tk.Label(frame, text="Age:")
age_label.grid(row=2, column=0)
age_label = tk.Entry(frame)
age_label.grid(row=2, column=1)

btn = tk.Button(frame, text="quit", command=root.destroy)
btn.grid(row=4, column=0)

btn = Button(frame, text="Submit", command=submit)
btn.grid(row=4, column=1)



root.mainloop()