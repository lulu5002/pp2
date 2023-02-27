import module as m

a = m.person1["age"]
print(a)

import platform
x = platform.system()
print(x)
y = dir(platform)
print(y)
#dir function caan be used for all modules

from module import person1
print(person1["name"])
