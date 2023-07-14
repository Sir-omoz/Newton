from tkinter import Tk, Label, Entry, Button

frame = LabelFrame(root, text="Welcome to Vicco Bank...", padx=60, pady=60)
frame.pack(padx=20, pady=20)


def check_balance():
    # Placeholder function for checking balance
    balance = 1000  # Replace with your actual balance retrieval logic
    balance_label.config(text=f"Balance: ${balance}")

def deposit():
    # Placeholder function for depositing money
    amount = float(deposit_entry.get())  # Get deposit amount from entry field
    # Add logic to update balance with the deposited amount
    # Example: balance += amount
    check_balance()  # Update balance label

def withdraw():
    # Placeholder function for withdrawing money
    amount = float(withdraw_entry.get())  # Get withdrawal amount from entry field
    # Add logic to update balance by deducting the withdrawal amount
    # Example: balance -= amount
    check_balance()  # Update balance label

root = Tk()
root.title("Bank App")

balance_label = Label(frame, text="Balance: $0.00")
balance_label.pack()

deposit_label = Label(root, text="Deposit Amount:")
deposit_label.pack()
deposit_entry = Entry(root)
deposit_entry.pack()

deposit_button = Button(root, text="Deposit", command=deposit)
deposit_button.pack()

withdraw_label = Label(root, text="Withdraw Amount:")
withdraw_label.pack()
withdraw_entry = Entry(root)
withdraw_entry.pack()

withdraw_button = Button(root, text="Withdraw", command=withdraw)
withdraw_button.pack()

check_balance()  # Initial balance check

root.mainloop()
