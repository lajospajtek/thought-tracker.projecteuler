#!/usr/bin/python
# -*- coding: latin-1 -*-
  
# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are 
# eight coins in general circulation:
#
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?
#
# ans: 73682

def step(sum, denom):
    total = 0
    if sum == 0: return 1
    if not denom: return 0
    c = denom[0]
    n = sum/c
    while n>=0:
        total += step(sum-n*c, denom[1:])
        n-=1
    return total

denom = (200, 100, 50, 20, 10, 5, 2, 1)
#denom = (200, 100, 50)

print step(200, denom)

