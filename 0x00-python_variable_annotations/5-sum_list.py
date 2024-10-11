#!/usr/bin/env python3
''' Module 5-sum_list.py '''


def sum_list(input_list: list[float]) -> float:
    total: float = 0.0
    for element in input_list:
        total += element
    return total
