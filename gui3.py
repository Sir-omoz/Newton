from tkinter import *
from tkinter import messagebox
from bank_account import SavingsAccount

# Create a savings account object
savings_account = SavingsAccount()

# Function to deposit money


def deposit_money():
    amount = float(deposit_entry.get())
    savings_account.deposit(amount)
    messagebox.showinfo("Success", f"Deposit of ${amount} was successful!")

# Function to withdraw money


def withdraw_money():
    amount = float(withdraw_entry.get())
    result = savings_account.withdraw(amount)
    if result == "success":
        messagebox.showinfo("Success", f"Withdrawal of ${amount} was successful!")
    else:
        messagebox.showerror("Error", result)

# Create the GUI window


root = Tk()
root.title("Savings Account")
root.geometry("400x300")

# Create the deposit frame
deposit_frame = LabelFrame(root, text="Deposit Money")
deposit_frame.pack(pady=20)

# Deposit entry box
deposit_entry = Entry(deposit_frame, font=("Helvetica", 24))
deposit_entry.pack(pady=20, padx=20)

# Deposit button
deposit_button = Button(deposit_frame, text="Deposit", command=deposit_money)
deposit_button.pack(pady=10)

# Create the withdraw frame
withdraw_frame = LabelFrame(root, text="Withdraw Money")
withdraw_frame.pack(pady=20)

# Withdraw entry box
withdraw_entry = Entry(withdraw_frame, font=("Helvetica", 24))
withdraw_entry.pack(pady=20, padx=20)

# Withdraw button
withdraw_button = Button(withdraw_frame, text="Withdraw", command=withdraw_money)
withdraw_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
##