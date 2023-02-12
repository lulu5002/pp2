students = ("Alua", "Almas", "Arman")
(smart, creative, clever) = students
print(smart)
print(creative)
print(clever)

students = ("Alua", "Almas", "Arman", "Daniyal")
(smart, creative, *clever) = students
print(smart)
print(creative)
print(clever)

students = ("Alua", "Almas", "Arman", "Daniyal")
(smart, *creative, clever) = students
print(smart)
print(creative)
print(clever)