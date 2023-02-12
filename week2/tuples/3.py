x = ("me", "I", "myself")
y = list(x)
y[1] = "you"
x = tuple(y)

print(x)

tuple1 = ("me", "I", "myself")
y = list(tuple1)
y.append("you")
tuple1 = tuple(y)

tuple2 = ("me", "I", "myself")
x = ("you",)
tuple2 += x

print(tuple2)

tuple3 = ("me", "I", "myself")
y = list(tuple3)
y.remove("apple")
tuple3 = tuple(y)

tuple4 = ("me", "I", "myself")
del tuple4
print(tuple4)

