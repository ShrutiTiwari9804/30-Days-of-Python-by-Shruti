import hashlib
import json 
import os

FILE_NAME = "vault.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_data():
    if not os.path.exists(FILE_NAME):
        return{}
    
    with open(FILE_NAME,"r") as file:
        return json.load(file)
    
def save_data(data):
    with open(FILE_NAME,"w") as file:
        json.dump(data, file, indent = 4)

def add_account(data):
    website = input("Website: ").lower()

    if website in data:
        print("Account already exists.")
        return
    
    username = input("Username/Email: ")
    password = input("Password: ")

    data[website] = {
        "username": username,
        "password_hash": hash_password(password)
    }

    save_data(data)
    print("Account saved securely.")


def view_accounts(data):
    if not data:
        print("Vault is empty.")
        return
    
    print("\nSaved Accounts\n")

    for site,info in data.items():
        print(f"Website: {site}")
        print(f"Username : {info['username']}")
        print(f"Hash     : {info['password_hash']}")
        print("-" * 40)

def verify_password(data):
    website = input("Website:  ").lower()

    if website not in data:
        print("Website not found.")
        return
    
    password = input("Enter password: ")

    if hash_password(password) == data[website]["password_hash"]:
        print("Password Verified")
    else:
        print("Incorrect Password")


def delete_account(data):
    website = input("Website : ").lower()

    if website in data:
        del data[website]
        save_data(data)
        print( "Deleted successfully.")
    else:
        print("Website not found.")

def menu():
    data = load_data()

    while True:
        print("\n===== PASSWORD VAULT =====")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Verify Password")
        print("4. Delete Account")
        print("5. Exit")


        choice = input("Enter choice:  ")

        if choice == "1":
            add_account()

        elif choice == "2":
            view_accounts()
        
        elif choice == "3":
            verify_password

        elif choice == "4":
            delete_account

        elif choice == "5":
            print("Vault Closed.")
            break

        else:
            print("Invalid Choice")

menu()

