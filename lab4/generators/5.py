def generator(n):
    for i in range(n, 0, -1):
        yield i
n = input()
list = [str(i) for i in generator(int(n))]
print(", ".join(list))