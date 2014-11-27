# ---------------------------------------------
#
# The file helpers is part of the gbgb project.  
# Copyright (c) 2014 Andrey Sobolev  
# License GNU GPL v.2
# See http://github.com/ansobolev/gbgb for details
#
# ---------------------------------------------
__author__ = 'andrey'

""" Helper functions for gbgb project
"""


def lcm(a, b, c):
    """
    Finds least common multiplier for numbers a, b, c
    :param a: a non-zero integer number
    :param b: a non-zero integer number
    :param c: a non-zero integer number
    :return: a positive integer number representing least common multiplier for (a,b,c) triple
    """
    def gcd(x, y):
        # Euclid algorithm
        while x:
            x, y = y % x, x
        return y

    def lcm2(x, y):
        return x * y / gcd(x, y)

    if a * b * c == 0:
        raise ValueError("lcm: arguments must be non-zero!")
    return abs(lcm2(a, lcm2(b, c)))
