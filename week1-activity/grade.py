# grade.py

# Dictionary containing student names and their grades
grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "D"
}

# Ask for the student's name
student_name = input("Enter the student's name: ")

# Print the student's grade
if student_name in grades:
    print(f"{student_name}'s grade is: {grades[student_name]}")
else:
    print(f"No grade found for {student_name}")