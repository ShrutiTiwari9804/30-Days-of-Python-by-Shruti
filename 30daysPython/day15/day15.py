import json
import os

class NoteManager:

    def __init__(self):
        self.file = "notes.json"
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                try:
                    self.notes = json.load(f)
                except :
                    self.notes = []

        else:
            self.save_notes()

    def save_notes(self):
        with open(self.file, "w") as f:
            json.dump(self.notes,f, indent = 4)

    def add_note(self):
        title = input("Title: ")
        content = input("Content: ")

        tags = input("Tags (comma separated): ").split(",")

        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "tags": [tag.strip().lower() for tag in tags]
        }

        self.notes.append(note)
        self.save_notes()

        print("Note Added Succesfully!")

    def view_notes(self):

        if not self.notes:
            print("No notes available.")
            return
        
        for note in self.notes:
            print("-" * 40)
            print("ID:", note["id"])
            print("Title:", note["title"])
            print("Content:", note ["content"])
            print("Tags:", ",".join(note["tags"]))

    def search_title(self):

        keyword = input("Enter title keyword:  ").lower()
        
        found = False

        for note in self.notes:
            if keyword in note ["title"].lower():
                print("-" * 40)
                print(note)
                found = True

        if not found:
            print("NO matching notes: ")

    def search_tag(self):

        tag = input("Enter tag: ").lower()

        found = False

        for note in self.notes:
            if tag in note ["tags"]:
                print ("-" * 40)
                print(note)
                found = True

        if not found:
            print("No notes with this tags.")

    def update_note(self):

        note_id = int(input("Enter Note ID: "))

        for note in self.notes:

            if note["id"] == note_id:

                note["title"] = input("New Title: ")
                note["content"] = input ("New Content: ")

                tags = input("New Tags (comma separated): ").split(",")

                note ["tags"] = [t.strip().lower() for t in tags]

                self.save_notes()

                print("Updated Successfully!")

        print ("Note not found.")

    def delete_note(self):

        note_id = int(input("Enter Note ID: "))

        for note in self.notes:

            if note["id"] == note_id:

                self.notes.remove(note)
                self.save_notes()

                print("Deleted Successfully!")
                return
            
        print ("Note Not Found.")

    def menu(self):

        while True:

            print("\n====== Notes Manager ======")
            print("1. Add Note")
            print("2. View Notes")
            print("3. Search by Title")
            print("4. Search by Title")
            print("5. Updated Note")
            print("6. Deleted Note ")
            print("7. Exist")

            choice = input("Choose: ")

            if choice == "1":
                self.add_note()

            elif choice == "2":
                self.view_notes()
            
            elif choice == "3":
                self.search_title()

            elif choice == "4":
                self.search_tag()

            elif choice == "5":
                self.update_note()

            elif choice == "6":
                self.delete_note()

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid Choice")

manager = NoteManager()
manager.menu()

        



























