#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# Non-abundant sums
# Problem 23
#
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
#
# Ans: 4179871


class Abundants(object):

    def __init__(self):
        self.abundants = []
        # (?) according to Wolfram Alpha, the practical limit is 20161
        for n in xrange(12, 20161+1): #20161-12):
            divs = self.proper_divisors(n)
            s = sum(divs)
            if s > n:
                self.abundants.append(n)

    @staticmethod
    def proper_divisors(i):
        pd = []
        for j in xrange(1, i/2+1):
            if i % j == 0:
                pd.append(j)
        return pd

    # this is O(n²) - todo optimize
    def is_sum_of_abundants(self, i):
        for a1 in self.abundants:
            if a1 > i:
                break
            for a2 in self.abundants:
                s = a1 + a2
                if s == i:
                    return True
                elif s > i:
                    break
        return False

    def __str__(self):
        return ",".join(map(str, self.abundants))


def main():
    abu = Abundants()
    ans = 0
    for i in xrange(1, 20162):
        if not abu.is_sum_of_abundants(i):
            print i
            ans += i
    print ans


if __name__ == "__main__":
    main()
