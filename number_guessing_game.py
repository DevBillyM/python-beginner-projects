# Function to display the menu
def display_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

# Function to add a new student
def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    student_id = len(students) + 1  # Generate a simple student ID
    
    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    print(f"Student {name} added with ID {student_id}.")

# Function to view all students
def view_students(students):
    if not students:
        print("No students available.")
    else:
        for student_id, info in students.items():
            print(f"ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")

# Function to update student information
def update_student(students):
    student_id = int(input("Enter student ID to update: "))
    
    if student_id in students:
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        
        students[student_id] = {
            "name": name,
            "age": age,
            "grade": grade
        }
        print(f"Student {student_id} updated.")
    else:
        print("Student ID not found.")

# Function to delete a student
def delete_student(students):
    student_id = int(input("Enter student ID to delete: "))
    
    if student_id in students:
        del students[student_id]
        print(f"Student {student_id} deleted.")
    else:
        print("Student ID not found.")

# Main function to manage the menu and actions
def student_management_system():
    students = {}  # Dictionary to store student data
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the student management system
if __name__ == "__main__":
    student_management_system()
