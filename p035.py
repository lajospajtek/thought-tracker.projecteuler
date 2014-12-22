#!/usr/bin/python
#
# Ans: 55

from bisect import bisect_left


class Primes1(object):

    def __init__(self):
        self.primes = []
        f = open("primes1.txt", "r")
        for line in f:
            self.primes.extend(map(int, line.split()))
        f.close()

    # from: https://docs.python.org/2/library/bisect.html
    def index(self, x):
        """Locate the leftmost value exactly equal to x"""
        i = bisect_left(self.primes, x)
        if i != len(self.primes) and self.primes[i] == x:
            return i
        return -1

    def is_prime(self, n):
        return self.index(n) != -1


def circulars(n):
    cl = []
    s1 = str(n)
    s2 = s1
    while s1:
        s2 = s2[1:]
        s2 += s1[0]
        s1 = s1[1:]
        cl.append(int(s2))
    return cl


def main():
    primes = Primes1()
    ans = 0
    for p in primes.primes:
        if p >= 1000000:
            break
        for r in circulars(p):
            if not primes.is_prime(r):
                break
        else:
            ans += 1
    print ans


if __name__ == "__main__":
    main()
