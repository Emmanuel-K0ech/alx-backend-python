#!/usr/bin/env python3
''' Module 6-sum_mixed_list.py '''

from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    ''' Mixed list of int and floats and returns their sum in float'''
    return float(sum(mxd_lst))
