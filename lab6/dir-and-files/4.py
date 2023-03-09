import os

filename = input("Enter the txt filename: ")


if os.path.isfile(filename):
    line_count = 0
    
    with open(filename, 'r') as file:
    
        lines = file.readlines()
        line_count = len(lines)
    print("The file contains", line_count, "lines.")
else:
    print("The file does  not exist.")
