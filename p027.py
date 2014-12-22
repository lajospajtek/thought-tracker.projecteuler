#!/usr/bin/python
#
# Ans: -59231
#
# Pure brute force approach...

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
    global primes
    return binary_search(primes, p) == -1


def is_prime(p):
    return not is_not_prime(p)


def main():
    global primes
    primes = read_primes("primes1.txt")
    print len(primes)
    max_n = max_a = max_b = -1
    for a in xrange(-1000,1001):
        for b in xrange(-999,1001,2):
            n = 1
            p = 3 # dummy value
            while is_prime(p):
                n += 1
                p = n * n + a * n + b
            n -= 1
            if max_n < n:
                max_n = n
                max_a = a
                max_b = b
                print max_a, max_b, max_n
    print max_a * max_b

primes = []
if __name__ == "__main__":
    main()
