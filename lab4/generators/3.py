def generate(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

k = int(input()) 
list = [str(i) for i in generate(k)]
print(", ".join(list))