"""
args_kwargs.py

Topics Covered

1. *args
2. **kwargs
3. Packing
4. Unpacking
"""


# ---------------- *args ---------------- #

def add_numbers(*numbers):

    total = 0

    for num in numbers:
        total += num

    return total


# ---------------- **kwargs ---------------- #

def student_information(**details):

    print()

    for key, value in details.items():

        print(f"{key} : {value}")


# ---------------- BOTH ---------------- #

def employee_information(name, *skills, **extra):

    print("\nEmployee Name :", name)

    print("\nSkills")

    for skill in skills:

        print("-", skill)

    print("\nAdditional Information")

    for key, value in extra.items():

        print(f"{key} : {value}")


# ---------------- UNPACKING ---------------- #

def multiplication(a, b, c):

    return a * b * c


def run_args_demo():

    print("\n------ *args Example ------")

    print(add_numbers(10, 20, 30, 40))

    print("\n------ **kwargs Example ------")

    student_information(
        Name="Shruti",
        Age=21,
        Course="Computer Engineering",
        Skill="Python"
    )

    print("\n------ *args + **kwargs ------")

    employee_information(
        "Shruti",
        "Python",
        "SQL",
        "FastAPI",
        City="Pune",
        Experience="Fresher"
    )

    print("\n------ Unpacking ------")

    numbers = [2, 3, 4]

    print(multiplication(*numbers))