from math import tan, pi
sides = int(input())
length = int(input())
p_area = sides * (length ** 2) / (4 * tan(pi / sides))
print(p_area)