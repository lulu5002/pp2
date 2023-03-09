from functools import reduce 
def multiply(nums):
    return reduce(lambda x, y: x*y, nums)

numbers = [2, 3, 4, 5]
result = multiply(numbers)
print(result)