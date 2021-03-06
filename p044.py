#!/usr/bin/python
# -*- coding latin-1 -*-

# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten
# pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 
# 70 - 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
# difference is pentagonal and D = |Pk - Pj| is minimised; what is the value 
# of D?
#
# ans: 5482660

def next_pentagonal():
  n = 0
  while True:
    n += 1
    yield n * (3 * n - 1) / 2

# use http://effbot.org/pyfaq/how-do-i-iterate-over-a-sequence-in-reverse-order.htm ??

pentagonals = []
ans = 99999999
for n in range(1,10000):
  pentagonals.append(n*(3*n-1)/2)
for p in pentagonals:
  for q in pentagonals:
    if q>p: break
    d = p-q
    #if (p-q) in pentagonals and (p+q) in pentagonals:
    if (p+q) in pentagonals and d in pentagonals:
      if d < ans: 
        ans = d
      print p, q, (p-q), (p+q)
      print "ans:", d
      exit(1)
print md

