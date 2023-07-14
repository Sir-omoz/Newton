import sqlite3
from tkinter import *


def create_account():
    account_number = account_number_entry.get()
    name = name_entry.get()
    initial_balance = float(balance_entry.get())

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO accounts (account_number, name, balance) VALUES (?, ?, ?)",
                   (account_number, name, initial_balance))

    conn.commit()
    conn.close()

    account_number_entry.delete(0, END)
    name_entry.delete(0, END)
    balance_entry.delete(0, END)

    status_label.config(text="Account created successfully!")


def get_account_balance():
    account_number = account_number_entry.get()

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    result = cursor.fetchone()

    conn.close()

    if result:
        balance = result[0]
        status_label.config(text=f"Account balance: {balance}")
    else:
        status_label.config(text="Account not found!")


def update_account_balance():
    account_number = account_number_entry.get()
    amount = float(amount_entry.get())

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    result = cursor.fetchone()

    if result:
        balance = result[0]
        new_balance = balance + amount
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                       (new_balance, account_number))

        conn.commit()
        conn.close()

        status_label.config(text="Account balance updated successfully!")
    else:
        conn.close()
        status_label.config(text="Account not found!")


# Create the main root
root = Tk()
root.title("Bank App")

# Create labels and entry fields
account_number_label = Label(root, text="Account Number:")
account_number_label.grid(row=0, column=0, padx=10, pady=5)
account_number_entry = Entry(root)
account_number_entry.grid(row=0, column=1, padx=10, pady=5)

name_label = Label(root, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=5)
name_entry = Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

balance_label = Label(root, text="Initial Balance:")
balance_label.grid(row=2, column=0, padx=10, pady=5)
balance_entry = Entry(root)
balance_entry.grid(row=2, column=1, padx=10, pady=5)

amount_label = Label(root, text="Amount:")
amount_label.grid(row=3, column=0, padx=10, pady=5)
amount_entry = Entry(root)
amount_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons
create_button = Button(root, text="Create Account", command=create_account)
create_button.grid(row=4, column=0, padx=10, pady=5)

get_balance_button = Button(root, text="Get Account Balance", command=get_account_balance)
get_balance_button.grid(row=4, column=1, padx=10, pady=5)

update_balance_button = Button(root, text="Update Account Balance", command=update_account_balance)
update_balance_button.grid(row=5, column=0, padx=10, pady=5)

# Create a status label
status_label = Label(root, text="")
status_label.grid(row=5, column=1, padx=10, pady=5)

# Run the main loop
root.mainloop()
