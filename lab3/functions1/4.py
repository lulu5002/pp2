def prime(n):
    if n <= 1:
        return "Not prime"
    else:
        for i in range(2, n):
            if n%i==0:
                return "Not prime"
            return "prime"
def filter_prime(list):
    prime_list = []
    for i in list:
        x = prime(i)
        if x == "prime":
            prime_list.append(i)
    return prime_list
print(filter_prime([2, 3, 5, 6, 78, 9]))