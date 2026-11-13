student_name = input("Enter Student Name: ")

mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

total_marks = mark1 + mark2 + mark3

average_marks = total_marks / 3


if average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
else:
    grade = "F"


print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")


