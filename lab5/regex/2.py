import re
file = open("C:/Users/aluao/OneDrive/Рабочий стол/test.txt", 'r', encoding = "utf8")
result = re.findall(r".*a+.*b+.*b+.*b*.*", file.read())
print(result)