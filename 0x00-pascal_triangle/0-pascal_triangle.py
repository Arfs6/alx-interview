#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """Creates a pascal triangle
    Parameters:
    - n: Number of rows in triangle
    Returns: A list containing lists that represent a row in the triangle.
    """
    if n <= 0:
        return []

    triangle = [
        [1],
    ]

    for curRow in range(1, n):
        newRow = [
            1,
        ]
        # Start from the first item in the previous row.
        # add it with it's next item
        # Stop at one number befor the last number
        for idx in range(1, curRow):
            curNum = triangle[curRow - 1][idx - 1] + triangle[curRow - 1][idx]
            newRow.append(curNum)
        newRow.append(1)
        triangle.append(newRow)

    return triangle
