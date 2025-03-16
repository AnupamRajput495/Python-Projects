import os
import shutil
import logging
import time
import tkinter as tk
from tkinter import filedialog

LOG_FILE = "file_organizer.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select Folder to Organize")

FOLDER_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Others": []
}

def get_unique_filename(destination, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(destination, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1

    return new_filename

def organize_files():
    global FOLDER_PATH
    FOLDER_PATH = select_folder() or FOLDER_PATH  

    if not os.path.exists(FOLDER_PATH):
        print(f"Folder not found: {FOLDER_PATH}")
        return

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(FOLDER_PATH, category)
                    os.makedirs(dest_folder, exist_ok=True)

                    new_filename = get_unique_filename(dest_folder, file)
                    shutil.move(file_path, os.path.join(dest_folder, new_filename))
                    logging.info(f"Moved {file} to {category} as {new_filename}")
                    print(f"Moved {file} to {category}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(FOLDER_PATH, "Others")
                os.makedirs(other_folder, exist_ok=True)

                new_filename = get_unique_filename(other_folder, file)
                shutil.move(file_path, os.path.join(other_folder, new_filename))
                logging.info(f"Moved {file} to Others as {new_filename}")
                print(f"Moved {file} to Others")

def undo_last_move():
    if not os.path.exists(LOG_FILE):
        print("No log file found. Cannot undo.")
        return

    with open(LOG_FILE, "r") as log:
        lines = log.readlines()

    if not lines:
        print("No moves recorded. Cannot undo.")
        return

    last_move = lines[-1]
    _, moved_file_info = last_move.strip().split(" - ")
    moved_file = moved_file_info.split("Moved ")[1]

    for category in FILE_CATEGORIES.keys():
        file_path = os.path.join(FOLDER_PATH, category, moved_file)
        if os.path.exists(file_path):
            shutil.move(file_path, FOLDER_PATH)
            print(f"Restored {moved_file} back to {FOLDER_PATH}")
            logging.info(f"Restored {moved_file} back to {FOLDER_PATH}")
            break

    with open(LOG_FILE, "w") as log:
        log.writelines(lines[:-1])  

def schedule_organizer():
    while True:
        print("🔄 Running file organizer...")
        organize_files()
        print("✅ Files Organized. Next run in 10 minutes.")
        time.sleep(600)  

if __name__ == "__main__":
    organize_files()  
    # schedule_organizer()