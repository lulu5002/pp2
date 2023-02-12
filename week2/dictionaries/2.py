student = {
    "name": "Alua",
    "relationships": False,
    "favcolors": ["red", "white", "blue"],
    "year": 2005,
    "nation": "kazakh"
}
x = student["name"]
y = student.get("relashionships")
z = student.keys()
print(x, y, z)

student = {
    "name": "Alua",
    "relationships": False,
    "year": 2005,
    "nation": "kazakh"
}
a = student.keys()
print(a)
student["favcolors"] = "red"
print(a)
x = student.values()
print(x)


student = {
    "name": "Alua",
    "relationships": False,
    "year": 2005,
    "nation": "kazakh"
}
y = student.values()
print(y)

student["year"] = 2004
print(y)

student = {
    "name": "Alua",
    "relationships": False,
    "year": 2005,
    "nation": "kazakh"
}
l = student.values()
print(l)

student["ab"] = "yes"
print(l)#after the change
print(student.items())


student = {
    "name": "Alua",
    "relationships": False,
    "year": 2005,
    "nation": "kazakh"
}
if "nation" in student:
    print("Yes, 'nation is one of the keys in the student dictionary")






