import os
import shutil

# Folder to organize
folder_path = "TestFolder"

# Categories
file_types = {
    "Images": [".jpg", ".jpeg" , ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ",mkv"],
    "Python Files": [ ".py"],
    "Archives": [".zip",".rar"]
}

def organize_files (folder):
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return
    
    files = os.listdir(folder)


    if not files:
        print("Folder is empty.")
        return
    moved = 0

    for file in files:
        file_path = os.path.join(folder, file)

        if os.path.isdir(file_path):
            continue


        extension = os.path.splitext(file)[1].lower()

        moved_file = False

        for category , extensions in file_types.items():
            if extension in extensions:
                category_folder = os.path.join(folder, category)

                os.makedirs(category_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(category_folder))

                print(f"Moved {file} → {category}")
                moved += 1
                moved_file = True
                break

        if not moved_file:
            others = os.path.join(folder, "others")
            os.makedirs(others, exist_ok=True)
            shutil.move(file_path,os.path.join(others, file))
            print(f"Moved {file} →  others")
            moved += 1

        print("\nOrganization Complete!")
        print(f"Total files moved: {moved}")


import os

print(os.getcwd())
print(os.path.exists(folder_path))

organize_files(folder_path)

