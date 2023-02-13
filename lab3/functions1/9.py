def volume(radius):
    fp = (4/3) * 3.142 
    sp = radius ** 3 
    v = fp * sp
    print(v)
volume(int(input()))