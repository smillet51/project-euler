#!/usr/bin/env python

"""
    A solution for problem 49 from Project Euler.
    https://projecteuler.net/problem=49

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is
    unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit
    numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
    property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import time

from primes import generate_list_of_primes, is_prime

def check_perms(first, second, third):
    """ Check if 3 numbers are permutations of one another. """

    one = sorted(str(first))
    two = sorted(str(second))
    three = sorted(str(third))

    if one == two and two == three and three == one:
        print "%s - %s - %s" % (first, second, third)

    
def problem_forty_nine():
    increase = 3330
    
    four_digit_primes = generate_list_of_primes(1000, 9999)

    for num in four_digit_primes:
        second = num + increase
        if second < (10000 - increase) and is_prime(second):
            third = num + (increase * 2)
            if third < 10000 and is_prime(third):
                check_perms(num, second, third)

if __name__ == "__main__":
    start = time.time()
    problem_forty_nine()
    end = time.time()

    print "Generating the solution took %f seconds" % (end - start)
