#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# Problem 46
# 20 June 2003
# 
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?


def binary_search(seq, t):
    min = 0; max = len(seq) - 1
    while 1:
        if max < min:
            return -1
        m = (min + max) / 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m

def read_primes(filename):
    prm = []
    f = open(filename, "r")
    for line in f:
        prm.extend(map(int, line.split()))
    return prm

def is_not_prime(p):
#    return not p in primes
    global primes
    return binary_search(primes, p) == -1

def is_prime(p):
    global primes
    return binary_search(primes, p) != -1

def main():
  global primes
  primes = read_primes("10000.txt")
  n = 1
  while n<25000000:
    n += 2
    if is_prime(n):
      continue
    m = 0
    done = False
    while not done:
      m += 1
      p = n - 2*m*m
      if p <=0:
        done = True
      if is_prime(p):
        print n, p, 2*m*m, m
	break
    else:
      print n
      exit(1)

primes = []
if __name__ == "__main__":
    main()

