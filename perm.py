from math import factorial
from itertools import permutations

def perm(n):
    print(factorial(n)) # find total number of permutations
    nums = list(range(1, n + 1))
    perms = permutations(nums) # find permutations
    for i in perms:
        print(" ".join(map(str, i))) # format output

print(perm(5))