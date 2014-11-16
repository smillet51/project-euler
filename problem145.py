#!/usr/bin/env python

"""
    A solution for problem 145 from Project Euler.
    https://projecteuler.net/problem=145

    Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of
    odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers
    reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n 
    or reverse(n).

    There are 120 reversible numbers below one-thousand.

    How many reversible numbers are there below one-billion (109)?
"""

import time

def problem145(exponent):
    count = 0

    # h/t to http://www.mathblog.dk/project-euler-145-how-many-reversible-numbers-are-there-below-one-billion/
    # for the insight into how to break down the problem more effectively
    # there is some duplication with 0 and 2 having the same function but i prefer the compactness of the
    # lambda expressions to having distinct functions defined for the 3 cases.
    digit_table = {0: lambda x: 20 * 30 ** (x / 2 - 1),
                   1: lambda x: 0,
                   2: lambda x: 20 * 30 ** (x / 2 - 1),
                   3: lambda x: 100 * 500 ** (x / 3 - 1)}

    # generate the range of exponents to check
    for i in xrange(1, exponent + 1):
        count += digit_table[i % 4](i)

    return count


if __name__ == "__main__":
    start = time.time()
    count =  problem145(3)
    end = time.time()
    print "found %s reversible numbers under 1000 in %f seconds" % (count, end - start) 

    start = time.time()
    count =  problem145(9)
    end = time.time()
    print "found %s reversible numbers under 1 billion in %f seconds" % (count, end - start)
