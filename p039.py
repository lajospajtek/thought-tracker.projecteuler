#!/bin/env python

# a^2 + b^2 = c^2
# a + b + c = p
# a + b - c > 0
# 
# p - c - c > 0
# p > 2c
# c < p/2
#
# p - a - b < p/2
# a + b > p/2
#
# ans: 840 (with 7 solutions)

def p039(p):
  i = 0
  print p, 
  for c in range (p/2, 1, -1):
    for a in range (1, p/4+1):
      b = p - a - c
      if a*a + b*b == c*c: 
        i += 1
        print "{", a, b, c, "}",
  print i
  return i

def main():
  nn = 0
  nm = 0
  for p in range (3, 1001):
    i = p039(p)
    if i > nn:
      nn = i
      nm = p
  print nm, nn

if __name__ == "__main__": main()

