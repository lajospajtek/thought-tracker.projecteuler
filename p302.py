#!/usr/bin/python
# -*- coding: Latin1 -*-

# Problem 302
# 18 September 2010
#
# A positive integer n is powerful if p^(2) is a divisor of n for every prime 
# factor p in n.
#
# A positive integer n is a perfect power if n can be expressed as a power of 
# another positive integer.
#
# A positive integer n is an Achilles number if n is powerful but not a 
# perfect power. For example, 864 and 1800 are Achilles numbers: 
# 864 = 2^(5)·3^(3) and 1800 = 2^(3)·3^(2)·5^(2).
#
# We shall call a positive integer S a Strong Achilles number if both S and 
# φ(S) are Achilles numbers.^(1)
# For example, 864 is a Strong Achilles number: φ(864) = 288 = 2^(5)·3^(2). 
# However, 1800 isn't a Strong Achilles number because: 
# φ(1800) = 480 = 2^(5)·3^(1)·5^(1).
#
# There are 7 Strong Achilles numbers below 10^(4) and 656 below 10^(8).
#
# How many Strong Achilles numbers are there below 10^(18)?
#
# ^(1) φ denotes Euler's totient function.

from math import sqrt, log

lim = 100000000

primes=[2,3]
i = 3
#slim=int(sqrt(lim))+1
slim=lim
#for i in range(5,lim,2):
while i < slim:
  i += 2
  l = int(sqrt(i))
  for d in primes[1:l]:
    if i % d == 0: break
  else: 
    primes.append(i)
  if i%10000 == 1 : print i

#print primes[999]

def is_powerful(n):
  #if n in primes:
  #  return False
  divs = []
  q = int(sqrt(n))
  for d in primes:
#    print d
#    if d > q: break
    if n % d != 0: continue
    rm = 0
    e = 0
    while True:
      dv, rm = divmod(n,d)
#      print ". ", n, d, dv, rm, e
      if rm != 0: break
      n = dv
      e += 1
    if e == 1: 
      divs = False
      break
    divs.append((d,e))
    #print d, e
  if divs == []: divs = [(n,1)]
  return divs

def is_achilles(n):
  divs = is_powerful(n)
  rc = False
  if divs != False: 
    rc = divs
    exps = [d[1] for d in divs]
    m = min(exps)
    for e in exps:
      if e%m != 0: 
        break
    else:
      rc = False
  return rc
  
def printdivs(n, divs):
  print n,
  for d in divs:
    print d[0], "^", d[1], 
  print

def totient(n, divs):
  rc = n
  for d in divs:
    rc = rc * (d[0]-1) / d[0]
  return rc
  

#divs = is_achilles(864)
#print totient(864, divs)
#exit()

ctr = 0
alist = []
for n in range(5,lim):
  divs = is_achilles(n)
  if divs == False: continue
  #alist.append(n)
  t =  totient(n, divs)
  tdivs = is_achilles(t)
  if tdivs == False: continue
  #if t in alist: 
  ctr += 1
  #print ctr, ":", n, divs, " - ", t
  print ctr, ":", n, divs, " - ", t, tdivs
  
#print alist
