def myfunc():
    x = 500
    print(x)

myfunc()

def myfunc1():
    x = 500
    def innerfunc():
        print(x)
    innerfunc()

myfunc1()

y = 300

def myfunc2():
    print(y)

myfunc2()
print(y)

x = 301
def myfunc3():
    x = 200
    print(x)
myfunc3()

print(x)

def myfunc4():
    global x
    x = 302
myfunc()
print(x)

z = 303

def myfunc5():
    global x
    x = 304

myfunc()

print(x)