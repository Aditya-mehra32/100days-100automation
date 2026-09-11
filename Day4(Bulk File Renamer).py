import os

# Folder containing the files
folder_path = "my_files"

# New name prefix
prefix = "File"

# Get all files
files = os.listdir(folder_path)

# Rename files
count = 1

for file in files:
    old_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isfile(old_path):
        extension = os.path.splitext(file)[1]

        new_name = f"{prefix}_{count}{extension}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

        print(f"Renamed: {file} → {new_name}")
        count += 1

print("\n✅ All files renamed successfully!")
