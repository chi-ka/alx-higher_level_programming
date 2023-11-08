#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding Python data structure."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle with 'n' rows.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        List of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            previous_row = triangle[-1]
            new_row = [1]

            for j in range(1, i):
                new_row.append(previous_row[j - 1] + previous_row[j])

            new_row.append(1)
            triangle.append(new_row)

    return triangle
