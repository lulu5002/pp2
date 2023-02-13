def has_33(x):
    for i in range(len(x) - 1):
        if x[i:i+2] == [3, 3]:
            print("True")
            return True
    print("False")
    return False
list = [1, 2, 3, 3, 4, 5]
has_33(list)