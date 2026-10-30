idli_stock = 20
dosa_stock = 15
print("1. Idli - Rs. 30")
print("2. Dosa - Rs. 50")
choice = int(input("Enter your choice: "))
quantity = int(input("Enter quantity: "))
if quantity <= 0:
    print("Invalid quantity")
elif choice == 1:
    if quantity <= idli_stock:
        bill = quantity * 30
        idli_stock = idli_stock - quantity
        print("Your Bill:", bill)
        print("Remaining Idli Stock:", idli_stock)
    else:
        print("Insufficient Idli Stock")
elif choice == 2:
    if quantity <= dosa_stock:
        bill = quantity * 50
        dosa_stock = dosa_stock - quantity
        print("Your Bill:", bill)
        print("Remaining Dosa Stock:", dosa_stock)
    else:
        print("Insufficient Dosa Stock")
else:
    print("Invalid Choice")