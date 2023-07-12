#!/usr/bin/python3
"""Moduile 12"""
def factorial(n):
    """Factorial function"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def pascal_triangle(n):
    """Pascal function"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        for j in range(n - i + 1):
            row = [
                factorial(i) // (factorial(i - j) * (factorial(j))) for j in range(i + 1)
            ]
        triangle.append(row)
    return triangle
