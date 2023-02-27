mytuple = ("apple", "cherry", "banana")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "Python"
myit1 = iter(mystr)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

mytuple = ("apple", "cherry", "banana")
for x in mytuple:
    print(x)

mystr = "Python"
for x in mystr:
    print(x)


class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Numbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Numbers1:
    def __iter__(self):
        self.a = 5
        return self
    def __next__(self):
        if self.a <= 15:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass1 = Numbers1()
myiter1 = iter(myclass1)

for x in myiter:
    print(x)