#!/usr/bin/python3

"""
Calculate the fewest number of operations needed to result in exactly n H characters in the file.
Returns: int: The minimum number of operations required.
Copy all and paste.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to obtain n H characters.
    
    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required.
    """
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
