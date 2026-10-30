budget = float(input("Enter your budget: "))
price1 = float(input("Enter first product price: "))
price2 = float(input("Enter second product price: "))
price3 = float(input("Enter third product price: "))
total = price1 + price2 + price3
print("Total Shopping Cost:", total)
if total <= budget:
    print("Shopping is within budget")
else:
    print("Shopping exceeds budget")
    extra = total - budget
    print("Amount exceeding budget:", extra)