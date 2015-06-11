# p063
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit 
# number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
#
# ans: 49

from math import log, floor

count=0
for b in range(1,10):
    for e in range(1,100):
        x = log(b**e,10)
        if floor(x+1) < e: break
        count=count+1
        print b, e, b**e, x, floor(x+1)==e

print "total:", count


