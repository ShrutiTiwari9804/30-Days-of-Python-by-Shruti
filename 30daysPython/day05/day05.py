students = []

def add_student():
    try:
        name = input("Enter student name: ").strip()
        age = input("Enter age: ")
        marks = float(input("Enter marks: "))

        student = {
            "Name" : name,
            "Age" : age,
            "Marks" : marks
        }


        students.append(student)
        print("\nStudent added successfully!\n")


    except ValueError:
        print("Invalid input ! Please enter the correct values." )


def display_students():
    if not students:
        print("\nNo student records found.\n")
        return
    

    print("\n--------Student Records--------")


    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Marks: {student['Marks']}")

def search_student():
    search_name = input("Enter student name: ").strip()

    found = False

    for student in students:
        if student['Name'].lower() == search_name.lower():
            print("\nStudent Found!")
            print(student)
            found = True
            break



        if not found :
            print("Student not found")


def update_marks():
    name = input("Enter student name: ")


    for student in students:
        if student ["Name"].lower() == name.lower():
            try:
                new_marks = float(input("Enter the marks: "))
                student["Marks"] = new_marks
                print("Marks updated successfully")
                return
            except ValueError:
                print("Invalid Marks.")
                return
        

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete.")

    for student in students :
        if student ["Name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            return
        
    print("Student not found.")




while True:


    print("\n======= Student Record System =======")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")


    choice = input("Enter your choices: ")


    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the Student Record System!")
        break

    else:
        print("Invalid choice. Please try again.")

