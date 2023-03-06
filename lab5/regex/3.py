import re
file = open('C:/Users/aluao/OneDrive/Рабочий стол/test.txt', 'r', encoding = "utf8")
result = re.findall(r"[a-z]+_[a-z]+", file.read())
print(result)