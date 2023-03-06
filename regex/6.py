import re
file = open('C:/Users/aluao/OneDrive/Рабочий стол/test.txt', 'r', encoding = "utf8")
result = re.sub("[ ,.]", ":", file.read())
print(result)