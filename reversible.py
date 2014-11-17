#!/usr/bin/env python

""" Some tools for dealing with reversible numbers for problem 145 from Project Euler.
    https://projecteuler.net/problem=145
"""


def is_odd(num):
    """ Check if an integer is odd. """
    if num % 2 != 0:
        return True
    else:
        return False


def is_reversible(num):
    """ Check if a number is reversible given the above definition. """

    if num % 10 == 0:
        return False

    num_str = str(num)
    rev_str = "".join(reversed(num_str))

    total = num + int(rev_str)

    for digit in str(total):
        if not is_odd(int(digit)):
            return False

    return True


if __name__ == "__main__":
    # check some odd and even numbers
    assert is_odd(1), "1 should be odd"
    assert not is_odd(2), "2 should not be odd"
    assert not is_odd(100), "100 should not be odd"
    assert is_odd(10001), "10001 should be odd"

    # check the example reversible numbers
    assert is_reversible(36), "36 should be reversible"
    assert is_reversible(63), "63 should be reversible"
    assert is_reversible(409), "409 should be reversible"
    assert is_reversible(904), "904 should be reversible"
        
    assert not is_reversible(10), "10 should not be reversible. (leading zero.)"

    print "all assertions passed"
