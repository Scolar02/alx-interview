#!/usr/bin/python3
"""
This module provides a function to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validates if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data: List of integers where each integer represents a byte (1-255).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    # Masks to check the first byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            # UTF-8 should not be more than 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Continuation bytes must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    # If num_bytes is not 0, the last character is incomplete
    return num_bytes == 0


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32,
             105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
