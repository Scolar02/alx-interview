#!/usr/bin/python3

"""
Calculate the fewest number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
