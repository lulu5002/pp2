fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "geeksforgeeks":
    print(x)


fruits = ["kiwi", "banana", "mango"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["kiwi", "banana", "mango"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["kiwi", "banana", "mango"]
for x in fruits:
  print(x)
  if x == "banana":
    continue
  print(x)

for x in range(10):
    print(x)

for x in range(3, 10):
    print(x)

for x in range(3, 10, 4):
    print(x)

for x in range(10):
    print(x)
else:
    print("Finally Finished!")

for x in range(12):
    if x == 6:
        break
else:
    print("Finally Finished!")
#if a loop stopped, the else block will NOT be executed

#nested loops
adj = ["tiny", "delicious", "sweet"]
fruits = ["kiwi", "mango", "blueberry"]

for x in adj:
    for y in fruits:
        print(x, y)

#pass statement
for x in [5, 6, 7]:
    pass




