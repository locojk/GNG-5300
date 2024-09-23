class Student:
    def __init__(self, name):
        self.name = name.strip().lower()
        self.grade = None

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

class StudentGrades:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        name = name.strip().lower()
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} added.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, name, grade):
        name = name.strip().lower()
        if name in self.students:
            self.students[name].set_grade(grade)
            print(f"Grade {grade} added for student {name}.")
        else:
            print(f"Student {name} does not exist.")

    def get_grade(self, name):
        name = name.strip().lower()
        if name in self.students:
            return self.students[name].get_grade()
        else:
            return f"Student {name} does not exist."

def main():
    student_grades = StudentGrades()
    while True:
        print("\nOptions: 1. Add Student 2. Add Grade 3. Get Grade 4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter student name: ").strip().lower()
            student_grades.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ").strip().lower()
            grade = input("Enter grade: ").strip()
            student_grades.add_grade(name, grade)
        elif choice == '3':
            name = input("Enter student name: ").strip().lower()
            print(f"Grade for {name}: {student_grades.get_grade(name)}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
