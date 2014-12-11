#/usr/bin/python
# vim: set fileencoding=UTF-8

# Problem 92
#
# A number chain is created by continuously adding the square of the digits in 
# a number to form a new number until it has been seen before.
#
# For example,
#
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
# loop. What is most amazing is that EVERY starting number will eventually 
# arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?
#
# ans: 8581146

# brute-force solution

def next_in_chain(i):
    sq = 0
    while i > 0:
        r = i % 10
        sq += r * r
        i /= 10
    return sq

def main():
    s89 = 0
    for i in xrange(2,10000000):
        sq = i
        while True:
            if sq == 1: break
            if sq == 89: 
                s89 += 1
                break
            print sq,
            sq = next_in_chain(sq)
        print sq
    print s89

if __name__ == "__main__": main()

