#!/usr/bin/python
# -*- coding latin-1 -*-

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
# of each of the digits 0 to 9 in some order, but it also has a rather 
# interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#    d2d3d4=406 is divisible by 2
#    d3d4d5=063 is divisible by 3
#    d4d5d6=635 is divisible by 5
#    d5d6d7=357 is divisible by 7
#    d6d7d8=572 is divisible by 11
#    d7d8d9=728 is divisible by 13
#    d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.
#
# ans: 16695334890


import itertools

def next_9_pandigital():
  #pp = itertools.permutations([9,8,7,6,5,4,3,2,1,0])
  pp = itertools.permutations([1,4,0,6,3,5,7,2,8,9])
  maxpd = -1
  for p in pp:
    if p == 0: break
    pandig = 0
    for d in p:
      pandig *= 10
      pandig += d
#    yield pandig
    if pandig > 1000000000: yield pandig
    else: continue

ans=0
for p in next_9_pandigital():
  if ((p)%1000)%17 != 0: continue
  if ((p/10)%1000)%13 != 0: continue
  if ((p/100)%1000)%11 != 0: continue
  if ((p/1000)%1000)%7 != 0: continue
  if ((p/10000)%1000)%5 != 0: continue
  if ((p/100000)%1000)%3 != 0: continue
  if ((p/1000000)%1000)%2 != 0: continue
  ans += p
  print p

print ans


