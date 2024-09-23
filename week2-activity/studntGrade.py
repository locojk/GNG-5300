grades = {}

def add_student(name):
    name = name.strip().lower()
    if name not in grades:
        grades[name] = None
        print(f"Student {name} added.")
    else:
        print(f"Student {name} already exists.")

def add_grade(name, grade):
    name = name.strip().lower()
    if name in grades:
        grades[name] = grade
        print(f"Grade {grade} added for student {name}.")
    else:
        print(f"Student {name} does not exist.")

def get_grade(name):
    name = name.strip().lower()
    if name in grades:
        return grades[name]
    else:
        return f"Student {name} does not exist."

def main():
    while True:
        print("\nOptions: 1. Add Student 2. Add Grade 3. Get Grade 4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter student name: ").strip().lower()
            add_student(name)
        elif choice == '2':
            name = input("Enter student name: ").strip().lower()
            grade = input("Enter grade: ").strip()
            add_grade(name, grade)
        elif choice == '3':
            name = input("Enter student name: ").strip().lower()
            print(f"Grade for {name}: {get_grade(name)}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
