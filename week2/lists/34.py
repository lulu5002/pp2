listofneeds = ["love", "eat", "pray", "fun", "education", "respect"]
newlist = [x if x != "love" else "fun" for x in listofneeds]
print(newlist)