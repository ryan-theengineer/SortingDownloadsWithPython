# Sort.py

This is a very simple project written in Python that automatically sorts your downloads folder into a clean list of sub-folders based on the file extension of the downloaded file.

Be sure to edit the script based on where your Downloads folder is located. On Linux and Mac be sure to know where they are located and add file extensions as needed.

You can run the script simply by cloning the Github repository and then running the following command in your terminal:

> python sort.py

If everything is set correctly such as pointing to your downloads folder, it should sort these files automatically based on file extension, and will even create the subdirectory if none exists. It will also handle naming conflicts by appending a number to the end of files that are already in the downloads folder.

It is incredibly easy to add file extensions to the script, simply edit the dictionary within the `sort.py` file.

If all goes well, it should print *"Files in the Downloads folder have been sorted into subfolders."* to the terminal and your files will be sorted.

Here is an example of file extensions you could add: 

```
file_extensions = {
    ".exe": "Executables",
    ".msi": "Executables",
    ".bat": "Executables",
    ".sh": "Executables",
    > ".tar": "Executables",
    > ".tgz": "Executables",
}
```

And so on. 

# Auto_sort_downloads.py 

This is a more advanced version of the sort.py script that allows you to automatically sort the downloads the moment they enter the folder. In order to run this script make sure you have Python installed and the latest version.

In your terminal (I recommend using Git Bash for Windows), simply run the following command 

> python auto_sort_downloads.py

This script will continually run until you close the terminal window, automatically running the sort.py script and placing your downloaded files into the correct subdirectory.

Thank you for viewing! 

I hope that you understand the basics of the script! If you have any questions or need help you can contact me at my website, [My Portfolio](https://strong-star.netlify.app)