thisset = {"pineapple", "mango", "cherry"}
thisset.remove("cherry")
print(thisset)

thisset1 = {"pineapple", "mango", "cherry"}
thisset1.discard("cherry")
print(thisset1)

#removing random item
thisset2 = {"pineapple", "mango", "cherry"}
x = thisset2.pop()
print(x)
print(thisset2)

thisset3 = {"pineapple", "mango", "cherry"}
thisset3.clear()
print(thisset)

thisset4 = {"pineapple", "mango", "cherry"}
del thisset4
print(thisset4)