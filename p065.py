#
#
# Problem 65
#
# ans: 272

from itertools import islice

# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#           ^
#           starts here. as teh fist two nominators (2,3) are given
def a_gen():
    n = 2
    while True:
        n += 1
        if n%3 == 0:
            yield 2*n/3
        else:
            yield 1


# From: https://en.wikipedia.org/wiki/Continued_fraction
# the nominator of a continued fraction can be expressed recursively as:
# h_n = a_n h_n-1 + h_n-2
def nominators():
    h_n2 = 2
    h_n1 = 3
    yield h_n2
    yield h_n1
    for a_n in a_gen():
        h_n = a_n * h_n1 + h_n2
        h_n2 = h_n1
        h_n1 = h_n
        yield h_n


# https://docs.python.org/2/library/itertools.html#recipes
def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s


print sum_of_digits(nth(nominators(), 99))
