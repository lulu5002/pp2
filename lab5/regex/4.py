import re
file = open('C:/Users/aluao/OneDrive/Рабочий стол/test.txt', 'r', encoding = "utf8")
result = re.findall(r"[A-Z]{1}[a-z]+", file.read())
print(result)