#!/usr/bin/env python

""" Tools for checking and generating prime numbers. """

import math

def is_prime(num):
    """ Test if a number is prime. """
    if num < 2:
        return False

    # take advantage of the speedup gained by only checking the sqrt
    sqrt = int(math.sqrt(num))

    # use xrange to generate the list as we iterate
    # use sqrt + 1 to handle smaller composites where the sqrt is 2.
    # we need an initial case to test fail out as False.
    for i in xrange(2, sqrt + 1):
        if num % i == 0:
            return False

    return True
    
def generate_list_of_primes(min, max):
    """ Given a min and max generate all the primes in that range. """
    assert max > min, "min %s is > than max %s" % (min, max)

    primes = []
    
    for x in xrange(min, max):
        if is_prime(x):
            primes.append(x)

    return primes

if __name__ == "__main__":
    # check for some simple prime and not prime numbers
    assert not is_prime(1), "1 should not be prime"
    assert is_prime(5), "5 should be prime"
    assert not is_prime(6), "6 should not be prime"
    assert not is_prime(100), "100 should be be prime"
    assert not is_prime(1000), "1000 should not be prime"

    # check the primes from the problem 49 example
    assert is_prime(1487), "1487 should be prime"
    assert is_prime(4817), "4817 should be prime"
    assert is_prime(8147), "8147 should be prime"

    for num in generate_list_of_primes(1, 100):
        assert is_prime(num), "%s should be prime" % num

    for num in generate_list_of_primes(1000, 9999):
        assert is_prime(num), "%s should be prime" % num

    print "all assertions passed"
