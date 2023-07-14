import tkinter as tk
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

def save_data():
    name = name_entry.get()
    age = age_entry.get()

    # Insert the data into the table
    cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

root = tk.Tk()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack()

root.mainloop()
