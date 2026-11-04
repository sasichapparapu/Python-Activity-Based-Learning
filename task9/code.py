students = []

number = int(input("How many students"))

for i in range(number):
    name = input("Student name: ")
    marks = [float(input(f"Subject {j + 1} marks: ")) for j in range(3)]
    attendance = float(input("Attendance percentage: "))
    income = float(input("Family income: "))
    students.append((name, marks, attendance, income))

eligible = []

for name, marks, attendance, income in students:
    average = sum(marks) / len(marks)

    if average >= 80 and min(marks) >= 60 and attendance >= 75 and income <= 500000:
        eligible.append((average, attendance, income, name))

eligible.sort(key=lambda student: (-student[0], -student[1], student[2]))

if eligible:
    print("\nScholarship ranking:")
    for rank, (average, attendance, income, name) in enumerate(eligible, start=1):
        print(rank, name, f"{average:.1f}%")
else:
    print("No students are eligible.")
