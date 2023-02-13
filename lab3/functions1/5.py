
from itertools import permutations
def allpermutations(str):
    permlist = permutations(str)
    for i in list(permlist):
        print(''.join(i))
allpermutations(str(input()))
    