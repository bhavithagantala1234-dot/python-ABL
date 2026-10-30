balance = float(input("Enter initial balance: "))
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
choice = int(input("Enter your choice: "))
if choice == 1:
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance = balance + amount
        print("Deposit Successful")
    else:
        print("Invalid amount")
elif choice == 2:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount")
    elif amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
elif choice == 3:
    print("Current Balance:", balance)
else:
    print("Invalid Choice")
print("Final Balance:", balance)