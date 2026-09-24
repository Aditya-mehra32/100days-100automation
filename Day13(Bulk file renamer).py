import os

folder = "C:/Users/YourName/Downloads"

for i, filename in enumerate(os.listdir(folder), start=1):
    old_path = os.path.join(folder, filename)

    if os.path.isfile(old_path):
        ext = os.path.splitext(filename)[1]
        new_name = f"file_{i}{ext}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)

print("Files renamed successfully!")
