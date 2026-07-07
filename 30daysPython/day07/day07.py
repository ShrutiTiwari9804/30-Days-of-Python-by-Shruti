import os


FILE_NAME = "expenses.txt"

def add_expense():
    """"Add a new expense to this file."""

    category = input("Enter Category (Food/Travel/Shopping/etc):").title()

    try:
        amount = float(input("Enter Amount (₹):"))
    except ValueError:
        print(" Invalid amount.\n")
        return

    note = input ("Enter Note: ").title()

    with open(FILE_NAME, "a") as file :
        file.write(f"{category},{amount},{note}\n")

    print("Expense Added Successfully\n")


def view_expenses():
    """"Display all expenses."""


    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return
    

    with open(FILE_NAME, "r") as file:
        records = file.readlines()


    if not records:
        print("No expenses available.\n")


    print("\n========== ALL EXPENSES ==========")

    total = 0

    for index, record in enumerate(records, start =1):
        category, amount, note = record.strip().split(",")


        print(f"{index}.{category}")
        print(f" Amount : ₹{amount}")
        print(f" Note : {note}\n")


        total += float(amount)

    print(f" Total Expenses : ₹{total:.2f}\n")


def search_category():
    """"Search expenses by category."""


    if not os.path.exists(FILE_NAME):
        print("No expense records found.\n")
        return
    
    search = input("Enter Category: ").title()


    found = False

    with open(FILE_NAME, "r") as file:

        for records in file :
            category, amount, note = record.strip().split(",")

            if category == search:
                found = True
                print(f"\nCategory : {category}")
                print(f"Amount : ₹{amount}")
                print(f"Note : {note}")
                print("---------------------------------")

    if not found:
        print("No matching category found.\n")

def menu():

    while True:

        print("""
=========== EXPENSE TRACKER ==========
1. Add Expense
2. View Expenses
3. Search by Category
4. Exit
======================================
""")
        
        choice = input("Enter choice: ")

        if choice =="1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_category()

        elif choice == "4":
            print(" Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid Choice!\n")

menu()