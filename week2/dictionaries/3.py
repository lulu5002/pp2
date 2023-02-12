student = {
    "name": "Alua",
    "relationships": False,
    "year": 2005,
    "nation": "kazakh"
}
student["nation"] = "turkish"
print(student)

student = {
    "name": "Alua",
    "relationships": False,
    "year": 2005,
    "nation": "kazakh"
}
student.update({"relashionships": "yes"})
print(student)