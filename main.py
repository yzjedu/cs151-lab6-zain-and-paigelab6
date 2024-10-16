
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
INITIAL_BALANCE = 1000
current_balance = INITIAL_BALANCE
SENTINEL = 'E'
choice = ''
def deposit():
    deposit_amount = input("Enter the amount to deposit: ").strip()

    if deposit_amount.isdigit():
        deposit_amount = int(deposit_amount)

        if deposit_amount < 0:
            print("Error: Please enter a positive number.")
        else:
            current_balance += deposit_amount
            print(f"Deposit successful! Your new balance is ${current_balance:.2f}.")
    else:
        print("Error: Please enter a valid number.")
        return INITIAL_BALANCE

def withdraw():
    withdraw_amount = input("Enter the amount to withdraw: ").strip()
    if withdraw_amount.isdigit():
        withdraw_amount = int(withdraw_amount)

     if withdraw_amount < 0:
                print("Error: Please enter a positive number.")
            else:
                current_balance -= withdraw_amount
                print(f"Withdrawal successful! Your new balance is ${current_balance:.2f}.")

                # Warning if the balance is negative
     if current_balance < 0:
                    print("❕ Warning: You have a negative balance. You will be charged 5% interest.")
        return INITIAL_BALANCE

    def View_Balance():
        return current_balance
    def exit():
        print('Thank you, this program is now over.')


# Start the loop until the user decides to exit
while choice.upper() != SENTINEL:
    # Display the menu
    if choice == D:
        deposit()
    elif choice == w:
        withdraw()
    elif choice == V:
        View_Balance()
    elif choice == E:
        exit()
    print("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit")

    choice = input("Your choice: ").strip().upper()




print("ATM program has ended.")