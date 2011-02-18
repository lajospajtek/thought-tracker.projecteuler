#!/usr/bin/python
# -*- coding: latin-1 -*-
  
# Problem 33
# The fraction ^(49)/_(98) is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly believe that
# ^(49)/_(98) = ^(4)/_(8), which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial 
# examples.

# There are exactly four non-trivial examples of this type of fraction, less 
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

# ans: 100

nn = dd = 1
for n1 in range(1,10):
  for n0 in range(1,10):
    if n1==n0: continue
    n = 10*n1+n0
    for d1 in range(1,10):
      for d0 in range(1,10):
        d = 10*d1+d0
        if n0==d1 and n*d0 == n1*d:
	  nn *= n
	  dd *= d
	  print n1, n0, "/", d1, d0
print nn, "/", dd

