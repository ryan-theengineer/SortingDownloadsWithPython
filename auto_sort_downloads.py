import os
import time
import shutil

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Define the sorting script to run
sorting_script = "sort.py"

# Create a dictionary to keep track of files and their modification times
file_modification_times = {}

while True:
    files = os.listdir(downloads_folder)

    for filename in files:
        source_file = os.path.join(downloads_folder, filename)
        last_modified = os.path.getmtime(source_file)

        # Check if the file is not in the dictionary or has been modified since last check
        if filename not in file_modification_times or last_modified > file_modification_times[filename]:
            file_modification_times[filename] = last_modified

            # Run the sorting script
            os.system(f"python {sorting_script}")

    # Wait for a while before checking again for downloads (e.g., every 5 seconds)
    time.sleep(5)

