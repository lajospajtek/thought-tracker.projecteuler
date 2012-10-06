#!/usr/bin/python
# -*- coding: latin-1 -*-

# Problem 47
# 
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct primes 
# factors. What is the first of these numbers?
#
# answer: 134043

from math import sqrt

maxn = 200000
maxp = maxn/2+1

primes=[2,3]
for i in range(5,maxp,2):
  l = int(sqrt(i))
  for d in primes[1:l+1]:
    if i % d == 0: break
  else: primes.append(i)

#pf1=[1]
#pf2=[2]
#pf3=[3]
d1 = d2 = d3 = 1
ddpf=4
i = 100000
while i<maxn:
  i += 1
  j = i
#  pf4=[]
  d4 = 0
  for p in primes:
    if p > j: break
    #if j % p == 0: pf4.append(p)
    if j % p == 0: d4 +=1
    while j % p == 0: j /= p
#  if len(pf4) == 4: print i, pf4
  #if len(pf4) == 4 and len(pf3) == 4 and len(pf2)==4 and len(pf1)==4:
  if d4 == 4 and d3 == 4 and d2==4 and d1==4:
#    print (i-3), pf1
#    print (i-2), pf2
#    print (i-1), pf3
#    print i, pf4
    break
#  pf1=pf2
#  pf2=pf3
#  pf3=pf4
  d1=d2
  d2=d3
  d3=d4

print "ans:", i-3
