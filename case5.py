mark1 = float(input("Enter first exam marks: "))
mark2 = float(input("Enter second exam marks: "))
mark3 = float(input("Enter third exam marks: "))
average = (mark1 + mark2 + mark3) / 3
print("Average Marks:", average)
if mark3 > mark1:
    print("Performance Improved")
elif mark3 < mark1:
    print("Performance Declined")
else:
    print("Performance Remained Same")
if average >= 75:
    print("Grade: Distinction")
elif average >= 60:
    print("Grade: First Class")
elif average >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")