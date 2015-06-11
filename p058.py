#

# Answer: 26241

from bisect import bisect_left
from miller_rabin import is_prime

sum = 1
n = 1
diag_total=1
diag_primes=0
for i in range(2,100000,2):
    for j in range (0,4):
        n += i
        diag_total = diag_total+1
        if is_prime(n):
            diag_primes = diag_primes + 1
#    print (i+1), diag_total, diag_primes, float(diag_primes)/diag_total, n
    if diag_primes*10 < diag_total: break

print "ans:", i+1
