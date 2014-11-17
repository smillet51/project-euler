#!/usr/bin/env python

"""
    A solution for problem 35 from Project Euler.
    https://projecteuler.net/problem=35

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and
    719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
"""

import time

from primes import generate_list_of_primes, is_circular_prime


def problem_thirty_five(total):
    count = 0
    
    primes = generate_list_of_primes(1, total)

    for num in primes:
        if is_circular_prime(num):
            count += 1

    print "Found %s primes under %s" % (count, total)

if __name__ == "__main__":
    start = time.time()
    problem_thirty_five(100)
    end = time.time()

    print "Solution for 100 primes took %f seconds" % (end - start)

    start = time.time()
    problem_thirty_five(10 ** 6)
    end = time.time()

    print "Solution for 1 million primes took %f seconds" % (end - start)
