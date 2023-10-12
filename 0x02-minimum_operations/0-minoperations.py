#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return n

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)

    return operations[n]
