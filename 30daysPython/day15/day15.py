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
        



























