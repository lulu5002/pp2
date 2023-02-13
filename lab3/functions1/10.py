def unique_list(n):
    x = []
    for a in n:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1, 1, 2, 3, 4, 6, 7, 7]))