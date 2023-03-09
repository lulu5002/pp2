import os 
path = 'C:/Users/aluao/OneDrive/Рабочий стол/pp2'
print("Directories and files:")
for dir_files in os.listdir(path):
    print(dir_files)
    
print("Directories:")
for dir_name in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir_name)):
        print(dir_name)

print("Files:")
for files_name in os.listdir(path):
    if os.path.isfile(os.path.join(path, files_name)):
        print(files_name)