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

