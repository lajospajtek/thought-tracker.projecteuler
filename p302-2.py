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

import operator
from math import sqrt, log
from fractions import gcd
from itertools import combinations

lim = 100000000
lim = int(1e5)

primes=[2,3]
slim=int(sqrt(lim))+1
slim=int(pow(lim, 1.0/3.0)*1.2)
for i in range(5,slim,2):
  l = int(sqrt(i))
  for d in primes[1:l]:
    if i % d == 0: break
  else: 
    primes.append(i)
  if i%10000 == 1 : print i-1

def is_achilles(n,exps):
  # by construction is already powerful
  return reduce(gcd, exps) == 1
  
def totient(n, divs):
  rc = n
  for d in divs:
    rc = rc * (d[0]-1) / d[0]
  return rc
  
def next_number(divs, exps):
  ld = len(divs)
  i = 0
  while True:
    exps[i] += 1
    m = 1
    for p, e in zip(divs,exps): m *= p ** e
    if m <= lim:
      return m
    else:
      exps[i] = 2
      i += 1
      if i == ld: return -1

ans = 0
alim = 80
an = []
for aa in range(2,alim):
  print "aa: ", aa
  m = primes[aa-1]
  for p in primes[0:aa]: m *= p*p
  if m > lim:
    print "! breaking at", aa
    break
  i = 0
  m = reduce(operator.mul, primes[:aa-1])
  m *= m
  r = 1
  while (m*r*r*r <= lim):
    r = primes[i+aa]
    i += 1
  print "max primes index:", i+aa, "next value:", r, "product:", m*r*r*r
    
  for divisors in combinations(primes[:i+aa],aa):
#    break
    exponents = [1] + (aa-2)*[2] + [3]
#    print " >>> ", divisors, exponents
    m = divisors[0] 
    for p, e in zip(divisors,exponents): m *= p ** e
    if m > lim: continue
    if divisors[-1] ** 3 > lim: 
      print "breakign for: ", divisors, exponents
      break
    while True:
      m = next_number(divisors, exponents)
      if m < 0: break
      if is_achilles(m, exponents):
        tdivs = list(divisors)
        tot = m
        for d in divisors: tot = tot * (d-1) / d
        texps = map(lambda x: x-1, exponents)
        tres = reduce(operator.mul, map(lambda x: x-1, divisors))
        tn = tres
        for d in primes:
          if tn % d != 0: continue
          if tn < d: break
          rm = 0
          e = 0
          while True:
            dv, rm = divmod(tn,d)
            if rm != 0: break
            tn = dv
            e += 1
          if d in tdivs:
            texps[tdivs.index(d)] += e
          else:
            tdivs.append(d)
            texps.append(e)
        if reduce(operator.and_, map(lambda x: x>1, texps)):
          if is_achilles(tot, texps):
            ans += 1
            print ans, m, divisors, exponents, "tot:", tot, tdivs, texps
            an.append(m)

print ">> achilles numbers below", lim, ":", ans 
an.sort()
print ",".join(map(str,an))
exit()

