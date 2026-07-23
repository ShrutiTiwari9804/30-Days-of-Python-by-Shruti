from decorators import run_decorator_demo
from closures import run_closure_demo
from args_kwargs import run_args_demo

while True:

    print("\n")
    print("=" * 50)
    print("ADVANCED PYTHON TOOLKIT")
    print ("=" * 50)

    print("1. Decorators")
    print("2. Closures")
    print("3. *args & **kwargs")
    print("4. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        run_decorator_demo()

    elif choice == "2":

        run_closure_demo()

    elif choice == "3":

        run_args_demo()

    elif choice == "4":

        print("\nThank You!")

        break

    else:

        print("\nInvalid Option")