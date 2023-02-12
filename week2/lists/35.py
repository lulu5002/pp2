listofneeds = ["love", "eat", "pray", "fun", "education", "respect"]
listofneeds.sort()
print(listofneeds)

listofnum = [123, 45, 890, 1000]
listofnum.sort()
print(listofnum)

list = ["love", "eat", "pray", "fun", "education", "respect"]
list.sort(reverse = True)
print(list)

listofnum1 = [123, 45, 890, 1000]
listofnum1.sort(reverse = True)
print(listofnum1)


def myfunc(n):
    return abs(n-14)
nums = [2, 35, 67, 13]
nums.sort(key = myfunc)
print(nums)

wtb = ["bread", "Milk", "Eggs", "sugar"]
wtb.sort()
print(wtb)


wtb1 = ["bread", "Milk", "Eggs", "sugar"]
wtb1.sort(key = str.lower)
print(wtb1)

wtb2 = ["bread", "Milk", "Eggs", "sugar"]
wtb2.reverse()
print(wtb2)
