#!/usr/bin/env python3
"""You have a text file with `h` in it.
Your text editor has only two operations, copy all and paste.
Find the minimum operations that will take to have `n` number of `h`.
"""


def getPeakFactor(num: int) -> int:
    """Return the factor of @num that has the highest result when @num is devided with it."""
    prevFactor = 1
    stop = num // 2
    for cur in range(1, stop + 1):
        if num % cur == 0:
            if num / cur == prevFactor:
                return prevFactor
            prevFactor = cur
    return prevFactor


def minOperations(n: int) -> int:
    """Solving the minimum operations problem.
    Parameters:
    - n: Number of `h` to get in the file.
    """
    if not isinstance(n, int):
        return 0
    elif n <= 1:
        return 0
    peakFactor = getPeakFactor(n)
    # print(n / minimum_operations(peakFactor))
    return int(n / peakFactor + minOperations(peakFactor))
