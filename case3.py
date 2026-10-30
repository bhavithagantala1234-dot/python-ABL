attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = attended / total * 100
    print("Attendance Percentage:", percentage)
    if percentage >= 75:
        print("Eligible for examination")
    else:
        extra = 0
        while (attended + extra) / (total + extra) * 100 < 75:
            extra += 1
        print("Extra classes required:", extra)