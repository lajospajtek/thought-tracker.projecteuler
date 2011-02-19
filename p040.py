#!/usr/bin/python
# -*- coding: Latin1 -*-

# Problem 40
# 28 March 2003

# An irrational decimal fraction is created by concatenating the positive 
# integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12^(th) digit of the fractional part is 1.
#
# If d_(n) represents the n^(th) digit of the fractional part, find the value 
# of the following expression.

# d_(1) × d_(10) × d_(100) × d_(1000) × d_(10000) × d_(100000) × d_(1000000)


c = 0
l = 1
d = 1
i = 1
while (c<=1000000):
  s = str(i)
  i += 1
  c += len(s)
  if c >= l:
    d *= int(s[l-c-1])
    l *= 10

print d
# ans = 210
