#!/usr/bin/env python3
"""
This is a Type-annotated function `add` that takes two variables a & b(float)
and returns their sum(float)
"""


def add(a: float, b: float) -> float:
    """ 
    Function returns the sum of a & b
    Args:
        a(float)
        b(float)
    Return: a + b -> float
    """
    return float(a + b)
