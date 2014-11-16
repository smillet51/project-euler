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
    for i in xrange(2, sqrt):
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
    print generate_list_of_primes(1, 100)
    print generate_list_of_primes(1000, 9999)
        
