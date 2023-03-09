import os
file_path = input("Enter a filename:")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("Permission denied: You do not have access to this file.")
else:
    print("File not found.")        