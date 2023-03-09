import os

path = input("Enter the path to check: ")

if os.path.exists(path):
    print("The path exists.")
    
    dirname, filename = os.path.split(path)
    print("Directory portion:", dirname)
    print("Filename portion:", filename)
else:
    print("The path does not exist.")