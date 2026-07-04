#--------------------------------------------------------------------------------
# Day 04 - Student Report Card Generator
# 30 Days Python Challenge
# Author : SHRUTI TIWARI
#--------------------------------------------------------------------------------




def calculate_grade (average):
    """" Returns grade according to average marks."""

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "Fail"

def get_marks(subjects):
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float (input(f"Enter marks in {subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            
            except ValueError:
                print("Please enter a valid number.")
    return marks


def display_report(student):
    print("/n" + "=" * 40)
    print("          STUDENT REPORT CARD")
    print("=" * 40)

    print(f"Name     : {student['name']}")
    print(f"Roll No. : {student['roll']}")

    print("\nSubject-wisw Marks")
    print("-" * 40)


    for subject, mark in zip(student["subjects"], student["marks"]):
        print(f"{subject :<20} {mark}")


    print ("-" * 40)
    print(f"Average : {student ['average']:.2f}")
    print(f"Grade   : {student ["grade"]} ")
    print("=" * 40)
    

def main():
    subjects = (
        "Python",
        "Mathematics",
        "Database",
        "English",
        "Computer Networks"
    )

    print("welcome tp Student Report Card Generator")

    name = input ("Enter the students name: ")
    roll = input ("Enter the roll name: ")

    marks = get_marks(subjects)

    average = sum(marks)/len(marks)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "subjects": subjects,
        "marks": marks,
        "average": average,
        "grade": grade
    }

    display_report(student)

main()
