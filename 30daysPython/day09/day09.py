import json 
import os

FILE_NAME = "books.json"

def load_books():
    if os.path.exists (FILE_NAME):
        with open (FILE_NAME,"r") as file:
            return json.load(file)
        return []
    

def save_books(books):
    with open (FILE_NAME,"w") as file:
        json.dump (books, file, indent=4)


def add_book (books):
    book_id = input ("Enter Book ID: ")

    for book in books :
        if book ["id"] == book_id:
            print ("Book ID already exists!")
            return
        
    title = input("Enter Book Title: ")
    author = input ("Enter Author Name: ")


    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    })

    save_books(books)
    print("Book Added successfully!")


def view_book(books):
    if not books:
        print("No Books Available.")
        return
    
    for book in books:
        status = "Issued" if book ["issued"] else "Available"


        print("-" * 35)
        print(f"Book ID : {book['id']}")
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print (f"Status : {status}")

    print("-" * 35)



def search_book(books):
    keyword = input ("Enter Book ID/Title/Author: ").lower()

    found = False

    for book in books:
        if (keyword in book ["id"].lower() or
                keyword in book ["title"].lower() or
                keyword in book ["author"].lower()): 

            status = "Issued" if book["issued"] else "Available"

        print("\n Book Found")
        print(f"Book ID : {book["id"]}")
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print (f"Status : {status}")

        found = True

    if not found:
        print ("Book not found.")


def issue_book (books):
    book_id = input("Enter Book ID: ")

    for book in books:
        if book['id'] == book_id:

            if book["issued"]:
                print("Book is already issued.")

            else:
                book["issued"] = True
                save_books(books)
                print("Book issued successfully.")
            return
        
        print("Book not found.")

def return_book(books):
    book_id = input ("Enter Book ID: ")

    for book in books:
            if book["id"] == book_id:

                if not book ["issued"]:
                    print("Book is already available.")

                else:
                    book["issued"] = False
                    save_books(books)
                    print("Book returned successfully.")

                return
            

    print("Book not found.")


def delete_book(books):
    book_id = input("Enter Book ID to delete: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)

def main():
    books = load_books()
    while True:

        print("""
              
1. Add Books
2. View Books
3. Search Book
4. Issue Book             
5. Return Book 
6. Delete Book
7. Exit
""")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            delete_book(books)
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

            


            
            
            
            
            
if __name__ == "__main__":
    main()

