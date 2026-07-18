import json
import os


class Transaction:
    """Represents a single income or expense transaction."""

    def __init__(self, transaction_id, transaction_type, amount, category, description):
        self.id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return{
            "id": self.id,
            "type": self.transaction_type,
            "amount": self.amount,
            "category": self.category,
            "description": self.description

        }

class PersonalFinanceSystem: 
    """Manages transaction and handles CRUD operations"""

    def __init__(self):
        self.folder = "finance_data"
        self.file = os.path(self.folder, "transaction.json")

        # Create folder and file if they don't exist
        os.makedirs(self.folder, exist_ok = True)

        if not os.path.exists(self.file):
            with open (self.file, "w") as f:
                json.dump([], f)

    def load_transactions(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def save_transaction(self, transactions):
        try:
            with open(self.file , "w") as f:
                json.dump(transactions, f, indent=4) 

        except PermissionError:
            print(" Permission denied while saving data.")

    # CREATE
    def add_transaction(self):
        transactions = self.load_transactions()

        try:
            transaction_id = len(transactions) + 1
            transaction_type = input("Enter type (income/expense):").lower()

            if transaction_type not in ["income", "expense"]:
                raise ValueError("Transaction type must be 'income' or 'expense'.")
            
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
            
            category = input("Enter category: ")
            description = input("Enter description: ")

            transaction = Transaction(
                transaction_id,
                transaction_type,
                amount,
                category,
                description
            )
        
            transaction.append(transaction.to_dict())
            self.save_transaction(transactions)

            print(" Transaction added successfully!")

        except ValueError as e:
            print(f"Invalid input: {e}")


    # READ

    def view_transactions(self):
        transactions = self.load_transaction()

        if not transactions:
            print(" No transactions found.")
            return
            
        print("\n==== Transaction ====")
        for t in transactions:
            print(
                f"ID : {t ['id']} | "
                f"Type : {t ['type']} | "
                f"Amount : {t ['amount']} | "
                f"Category : {t ['category']} | "
                f"Description : {t ['description']} | "
                )
    
    # UPDATE
    def update_transaction(self):
        transactions = self.load_transactions()

        try:
            transaction_id = int(input("Enter transaction ID to update: "))

            for t in transactions:
                if t["id"] == transaction_id:
                    t["amount"] == float (input ("Enter new amount: "))
                    t["category"] == input("Enter new category : ")
                    t["description"] == input("Enter new description : ")

                    self.save_transactions(transactions)
                    print(" Transaction updated successesfully!")
                    return
                
                print(" Transaction not found.")

        except ValueError:
            print (" please enter valid numeric values.")

    
    # DELETE
    def delete_transaction(self):
        transactions = self.load_transactions()

        try:
            transaction_id = int(input("Enter transaction ID to delete: "))

            new_transactions = [t for t in transactions if t["id"] != transaction_id]

            if len(new_transactions) == len(transactions):
                print("❌ Transaction not found.")
            else:
                self.save_transactions(new_transactions)
                print("✅ Transaction deleted successfully!")

        except ValueError:
            print("❌ Please enter a valid transaction ID.")

    # REPORT
    def generate_report(self):
        transactions = self.load_transactions()

        total_income = sum(
            t["amount"] for t in transactions if t["type"] == "income"
        )
        total_expense = sum(
            t["amount"] for t in transactions if t["type"] == "expense"
        )
        savings = total_income - total_expense

        print("\n===== Finance Report =====")
        print(f"Total Income : ₹{total_income}")
        print(f"Total Expense: ₹{total_expense}")
        print(f"Savings      : ₹{savings}")

    def menu(self):
        while True:
            print("\n===== Personal Finance System =====")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Update Transaction")
            print("4. Delete Transaction")
            print("5. Generate Report")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.view_transactions()
            elif choice == "3":
                self.update_transaction()
            elif choice == "4":
                self.delete_transaction()
            elif choice == "5":
                self.generate_report()
            elif choice == "6":
                print("👋 Exiting program. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    system = PersonalFinanceSystem()
    system.menu()




