import os
import shutil

# Define the source and destination folders
downloads_folder = os.path.expanduser("~/Downloads")

# Create sub-folders for each file extension category
file_extensions = {
    ".exe": "Executables",
    ".msi": "Executables",
    ".bat": "Executables",
    ".sh": "Executables",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".jpg": "Photos",
    ".jpeg": "Photos",
    ".png": "Photos",
    ".gif": "Photos",
    ".webp": "Photos",
    ".pdf": "PDFs",
    ".zip": "Archives",
    ".iso": "Archives",
    ".rar": "Archives",
    ".txt": "Text",
    ".md": "Text",
    ".json": "JSON",
}

# Create the sub-folders if they don't exist
for folder in file_extensions.values():
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Get a list of files in the Downloads folder
files = os.listdir(downloads_folder)

# Move files to their respective folders based on their extensions
for filename in files:
    source_file = os.path.join(downloads_folder, filename)
    file_extension = os.path.splitext(filename)[1].lower()

    # Check if the file extension is in the dictionary
    if file_extension in file_extensions:
        destination_folder = os.path.join(downloads_folder, file_extensions[file_extension])
        destination_file = os.path.join(destination_folder, filename)

        # Handle file name conflicts
        if os.path.exists(destination_file):
            base, ext = os.path.splitext(filename)
            i = 1
            while os.path.exists(os.path.join(destination_folder, f"{base}_{i}{ext}")):
                i += 1
            destination_file = os.path.join(destination_folder, f"{base}_{i}{ext}")

        # Move the file to the destination folder
        shutil.move(source_file, destination_file)

print("Files in the Downloads folder have been sorted into subfolders.")
