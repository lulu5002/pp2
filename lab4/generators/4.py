def squares(m, n):
    for i in range(m, n + 1):
        yield i*i
a = input()
b = input()
list = [str(i) for i in squares(int(a), int(b))]
print(", ".join(list))