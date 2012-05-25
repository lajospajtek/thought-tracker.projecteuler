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

def truncate_l2r(p):
    s = 1
    while p/s > 10:
        s *= 10
#    print p, s, divmod(p,s)

    while s > 1:
        p = p % s
        s /= 10
#        print "left: ", p
        if is_not_prime(p): return False
    return True

def truncate_r2l(p):
#    print p
    while True:
        p /= 10
        if p == 0: return True
#        print "right:", p
        if is_not_prime(p): return False
    return True

def main():
  global primes
  primes = read_primes("primes1.txt")
  psum = 0
  pnum = 0
  for prime in primes:
    if prime < 10: continue
    if truncate_l2r(prime) and truncate_r2l(prime):
        psum += prime
        print prime, psum
        pnum += 1
        if pnum == 11: break

primes = []
if __name__ == "__main__":
    main()

