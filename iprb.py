def iprb(k, m, n):
    # k = homozygous dominant
    # m = heterozygous
    # n = homozygous recessive
    total = k + m + n
    prob = ( 
        2*((((k*m) / (total*(total-1)))) * (1/1)) # k,m
      + 2*((((k*n) / (total*(total-1)))) * (1/1)) # k,n
      + 2*((((m*n) / (total*(total-1)))) * (1/2)) # m,n
      + (((k*(k-1)) / (total*(total-1)))) * (1/1) # k,k
      + (((m*(m-1)) / (total*(total-1)))) * (3/4) # m,m
      + (((n*(n-1)) / (total*(total-1)))) * (0/1) # n,n
    )
    return prob

print(iprb(25, 23, 23))