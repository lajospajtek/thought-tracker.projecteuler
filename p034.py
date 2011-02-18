#!/usr/bin/python
# -*- coding: latin-1 -*-
  
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of 
# their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# ans: 40730

f=(1,1,2,6,24,120,720,5040,40320,362880)

def sdf(i):
    dv=i
    n=0
    while dv>0:
        dv, rm = divmod(dv,10)
        n+=f[rm]
    return i if n == i else False

#sum=0
#for i in range(3,100000): # should be one more 0
#    if sdf(i): 
#        sum += i
#        print i
#
#print "ans:", sum

print reduce(lambda x,y: x+y, map(sdf, range(3,100000)))
