listofneeds = ["love", "eat", "pray", "fun", "education", "respect"]
newlist = []

for x in listofneeds:
    if "e" in x:
        newlist.append(x)

print(newlist)

#with comprehension:
listofneeds = ["love", "eat", "pray", "fun", "education", "respect"]

newlist = [x for x in listofneeds if "e" in x]
print(newlist)

"""
the syntax is such 
newlist = [expression for item in iterable if condition == True]
"""
 
