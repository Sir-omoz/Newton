from tkinter import *
import sqlite3

root = Tk()

# Create a SQLite database connection
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

def retrieve_data():
    # Retrieve data from the table
    cursor.execute("SELECT * FROM my_table")
    data = cursor.fetchall()

    # Display the retrieved data using Tkinter
    for row in data:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("")


retrieve_data()

root.mainloop()