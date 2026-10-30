students = ["Student 1", "Student 2", "Student 3"]
marks = []
for student in students:
    mark1 = int(input("Enter Python marks: "))
    mark2 = int(input("Enter Maths marks: "))
    mark3 = int(input("Enter English marks: "))
    marks.append([mark1, mark2, mark3])
for i in range(len(students)):
    total = sum(marks[i])
    average = total / 3
    print(students[i])
    print("Total Marks:", total)
    print("Average Marks:", average)
totals = [sum(row) for row in marks]
top = totals.index(max(totals))
print("Top Performer:", students[top])