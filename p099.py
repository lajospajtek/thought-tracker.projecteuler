# project euler problem 099

# ans = 709

from math import log

def read_tuples(filename):
    be = []
    file = open(filename)
    for line in file:
        a = line.strip().split(",")
        if a == ['']: break
        base, expo = a
        be.append((float(base), float(expo)))
    return be

bel = read_tuples("p099_base_exp.txt")

i = 0
mark = -1
for be in bel:
    i += 1
    base, expo = be
    crt = expo * log(base)
    if crt > mark:
        mark = crt
        print i, mark, be

