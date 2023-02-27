def evennums(n):
    i = 0
    while i < n:
        if i % 2 == 0:
            yield i
        i+=1
k = int(input())
values = []
for i in evennums(k):
    values.append(str(i))
print(", ".join(values))
