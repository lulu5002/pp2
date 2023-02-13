primes = [2,3,4,6,7,9,10,15,20,23,17,39,27,49,100]
for i in range(2, 8): 
    primes = list(filter(lambda x: x == i or x % i!=0, primes))
print(*primes)

