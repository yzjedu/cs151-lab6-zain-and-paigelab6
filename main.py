# Programmers:  [Zain, Paige]
# Course:  CS151, [Instructors name here]
# Due Date: [date assignment is due]
# Programming Assignment:  [Lab 6]
# Problem Statement:  [Refinning Lab 5 by integrating functions]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program
from logging import DEBUG

print("Welcome to the ATM program! This program allows you to interact with your account balance.")

# Initialize variables
initial_balance = 1000
current_balance = initial_balance
SENTINEL = 'E'

def deposit():
    initial_balance = 1000
    current_balance = initial_balance
    deposit_amount = input("Enter the amount to deposit: ").strip()
    while not deposit_amount.isdigit():
        print("Please enter a valid deposit amount.")
        deposit_amount = input("Enter the amount to deposit: ").strip()
    deposit_amount = int(deposit_amount)
    while deposit_amount < 0:
        print("Error: Please enter a positive number.")
        deposit_amount = input("Enter the amount to deposit: ").strip()
    current_balance += deposit_amount
    initial_balance = current_balance
    print(f"Deposit successful! Your new balance is ${current_balance:.2f}.")
    return current_balance


def withdraw():
    initial_balance = 1000
    current_balance = initial_balance
    withdraw_amount = input("Enter the amount to withdraw: ").strip()
    while not withdraw_amount.isdigit():
        print("Please enter a valid withdraw amount.")
        withdraw_amount = input("Enter the amount to withdraw: ").strip()
    withdraw_amount = int(withdraw_amount)
    while withdraw_amount < 0:
        print("Error: Please enter a positive number.")
        withdraw_amount = input("Enter the amount to withdraw: ").strip()

    current_balance -= withdraw_amount
    initial_balance = current_balance
    print(f"Withdrawal successful! Your new balance is ${current_balance:.2f}.")

    # Warning if the balance is negative
    if current_balance < 0:
        print("❕ Warning: You have a negative balance. You will be charged 5% interest.")
    return current_balance

def View_Balance():
    print(f"Your balance is ${current_balance:.2f}.")
    return current_balance
def exit():
    print('Thank you, this program is now over.')


# Start the loop until the user decides to exit
def main():
    initial_balance = 1000
    current_balance = initial_balance
    SENTINEL = 'E'
    choice = ''
    while choice.upper() != SENTINEL:
        # Display the menu
        print("\nPlease select an option:"
              "\n\t D - Deposit"
              "\n\t W - Withdraw"
              "\n\t V - View Balance"
              "\n\t E - Exit")

        choice = input("Your choice: ").strip().upper()

        if choice == 'D':
            deposit()
            initial_balance = current_balance
        elif choice == 'W':
            withdraw()
            initial_balance = current_balance
        elif choice == 'V':
            View_Balance()
        elif choice == 'E':
            exit()


main()

print("ATM program has ended.")