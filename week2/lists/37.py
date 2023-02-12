#join lists

list1 = [123, 456, 789]
list2 = ["hello", "it", "is", "numbers"]

list3 = list1 + list2
print(list3)

list1 = [123, 456, 789]
list2 = ["hello", "it", "is", "numbers"]
for x in list2:
    list1.append(x)
print(list1)

list1 = [123, 456, 789]
list2 = ["hello", "it", "is", "numbers"]
list1.extend(list2)
print(list1)