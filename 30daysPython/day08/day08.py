import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open (FILE_NAME, "r") as file:
        return json.load(file)
    

def save_contacts (contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Name : ")
    phone = input ("Phone: ")
    email = input("Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("\nContact Added Sucessfully!\n")


def view_contact(contacts):
    if not contacts:
        print("\nNo Contact Found.\n")
        return
    

    print("\n-------- CONTACT LIST --------")

    for i , contact in enumerate(contacts,start=1):
        print(f"""
{i}.
Name : {contact['name']}
Phone : {contact['phone']}
Email : {contact["email"]}
"""
)
        

def search_contact(contacts):
    keyword = input ("Enter Name : ").lower()

    found = False

    for contact in contacts:
        if keyword in contact ["name"].lower():
            print(f"""
Name : {contact['name']}                 
Phone : {contact [ 'phone']}           
Email :  {contact [ 'email']}            
"""                 
)
            found = True


    if not found :
        print("Contact not found.")


def delete_contact(contacts):
    if contact["name"].lower() == name :
        contacts.remove(contact)
        save_contacts(contacts)
        print("Deleted Successfully.")
        return
    
    print("Contact not found.")


def update_contact(contacts):
    name = input("Enter Name to Update: ").lower()


    for contact in contacts:

        if contact["name"].lower() == name:
        
            
            contact["phone"] = input("New Phone: ")
            contact["email"] = input("New Email")

            save_contacts(contacts)
            print("Updated Successfully.")
            return
        

        print("Contact not found.")


def main():

    contacts = load_contacts()

    while True:
        p