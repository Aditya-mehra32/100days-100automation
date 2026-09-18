import os
import shutil

folder = "Downloads"

folders = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".zip": "Archives"
}

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path):
        ext = os.path.splitext(file)[1].lower()

        if ext in folders:
            destination = os.path.join(folder, folders[ext])
            os.makedirs(destination, exist_ok=True)
            shutil.move(path, os.path.join(destination, file))

print("Files organized successfully!")
