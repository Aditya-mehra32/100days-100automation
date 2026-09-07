import os
import shutil

# Target directory to organize, relative to this script
TARGET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_files")

# Map folder names to file extensions
EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Archives": [".zip", ".tar", ".rar", ".gz"],
}


def organize_folder(directory):
    os.makedirs(directory, exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip subdirectories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find matching category
        moved = False
        for folder_name, ext_list in EXTENSIONS.items():
            if ext in ext_list:
                dest_dir = os.path.join(directory, folder_name)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_dir, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break

        # Send unrecognized files to an 'Others' folder
        if not moved and ext:
            dest_dir = os.path.join(directory, "Others")
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, filename))
            print(f"Moved: {filename} -> Others/")


if __name__ == "__main__":
    organize_folder(TARGET_DIR)
