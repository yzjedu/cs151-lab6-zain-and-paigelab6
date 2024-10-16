
1. Output a welcome message explaining the purpose of the program.
2. Initialize variables:
    - `INITIAL_BALANCE = 1000`
    - `current_balance = INITIAL_BALANCE`
    - `SENTINEL = 'E'` (to exit the loop)
    - `choice = ''` (to store user’s menu choice)
3. Make a function named deposit:
   4. prompt user how much they want to deposit 
   2. Check if the deposit amount is a valid positive integer:
          1. Convert the input to an integer.
          1. If the amount is positive, add it to `current_balance`.
          1. Display the new balance to the user.
   3. otherwise:
         1. Output an error message requesting a valid positive number.
   4. return `current_balance`
4. make a function named withdraw:
   1. Prompt the user to enter the amount to withdraw.
   2. Check if the withdrawal amount is a valid positive integer:
      1. Convert the input to an integer.
      1. If the amount is positive, subtract it from `current_balance`.
      1. Display the new balance to the user.
   1. If the `current_balance` becomes negative:
      1.  Output a warning message indicating that the user will be charged 5% interest.
   3. otherwise:
      1. Output an error message requesting a valid positive number.
   4. return `current_balance`
5. make a function named view_balance:
   1. return `current_balance`
6. make a function named exit:
   7. Output a message thanking the user and indicate the program is ending.
7. while loop that continues until the user enters 'E':
   1. if the choice is 'D':
      1. call deposit function 
   2. else if the choice is 'W':
      1. call withdraw function
   3. else if the choice is 'V':
      1. call view_balance function
   4. else if choice is 'E':
      1. call exit function
   5. Otherwise, if the choice is not one of the valid options:
      1. Output an error message requesting a valid option (D, W, V, or E)
5. Output a message indicating the ATM program has ended.