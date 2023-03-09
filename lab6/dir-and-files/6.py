import string
import os

letters = string.ascii_uppercase

for letter in letters:
    file_name = letter + ".txt"
    open(file_name, "w").close()
    print("Created file:", file_name)
    
files = os.listdir()
txt_files = [file for file in files if file.endswith(".txt")]
assert len(txt_files) == 26, "Error: not all files were created"
print("All files were created successfully.")