from math import factorial
from itertools import permutations

def perm(n):
    print(factorial(n))
    nums = list(range(1, n + 1))
    perms = permutations(nums)
    for i in perms:
        print(" ".join(map(str, i)))

print(perm(5))