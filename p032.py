#!/usr/bin/python
# -*- coding: latin-1 -*-
  
# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only 
# include it once in your sum.
#
# ans: 45228

def digit_list(nn, ll):
    while True:
        nn, rm = divmod(nn,10)
	if rm!=0 and rm not in ll: # not 0 and was not seen before 
	    ll.append(rm)
	else: 
	    return []
	    break
	if nn==0: break
    return ll 

s=[]
for i in range(1,10000):
    l1 = digit_list(i, [])
    if not l1: continue
    for j in range(1,100):
        l2 = digit_list(j,list(l1)) # passing a copy of l1
	if not l2: continue
	p = i*j
        if p>10000: break # a bit of cheating ...
	l = digit_list(p,l2)
	if not l: continue
	if len(l) != 9: continue
        if p in s: continue
	s.append(p)
	print i, j, p, l

#print s
print sum(s)
