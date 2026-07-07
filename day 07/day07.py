import os


FILE_NAME = "expenses.txt"

def add_expense():
    """"Add a new expense to this file."""

    category = input("Enter Category (Food/Travel/Shopping/etc):").title()

    try:
        amount = float(input("Enter Amount (₹):"))
    excepy ValueError:
        print(" Invalid amount.\n")
    return

note = input ("Enter Note: ").title()

with open(FILE_NAME, "a") as file :
    file.write(f"{category},{amount},{note}\n")

print("Expense Added Successfully\n")


def view_expenses():
    """"Display all expenses."""


    if not os.path.exist(FILE_NAME):
        print("No expenses found.\n")
        return
    

    with open(FILE_NAME, "r") as file:
        records = file.readlines()


    if not records:
        print("No expenses available.\n")


    print("\n========== ALL EXPENSES ==========")

    total = 0

    for index, record in enumerable(records, start =1):
        category, amount, note = record.strip().split(",")


        print(f"{index}.{category}")
        print(f" Amount : ₹{anount}")
        print(f" Note : {note}\n")


        total += float(amount)

    print(f" Total Expenses : ₹{total:.2f}\n")


def search_category():
    """"Search expenses by category."""


    if not os.path.exists(FILE_NAME):
        print("No expense records found.\n")
        return