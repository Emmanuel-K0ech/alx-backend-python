#!/usr/bin/env python3
'''
Module 7-to_kv.py - to_kv()
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple:
    ''' Takes a string and number (int or float) and returns a tuple.
        The tuple contains the string and the square of the number as a float.
    '''
    result_tuple: Tuple[str, float] = (k, (v * v))
    return result_tuple
