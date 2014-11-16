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
from reversible import is_reversible


def problem145(max=1000):
    count = 0
    
    for number in xrange(1, max):
        if is_reversible(number):
            count += 1

    return count

if __name__ == "__main__":
    start = time.time()
    count =  problem145()
    end = time.time()
    print "found %s reversible numbers under 1000 in %f seconds" % (count, end - start) 

    start = time.time()
    count =  problem145(max=10 ** 9)
    end = time.time()
    print "found %s reversible numbers under 1000 in %f seconds" % (count, end - start) 
