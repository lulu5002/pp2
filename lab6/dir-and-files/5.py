my_list = input("Enter a list of strings separated by spaces: ").split()
filename = input("Enter a filename: ")
with open(filename, 'w') as file:
    for item in my_list:
        file.write(item + '\n')
print("List written to file successfully.")
