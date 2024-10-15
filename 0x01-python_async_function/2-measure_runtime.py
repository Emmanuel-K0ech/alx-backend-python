#!/usr/bin/env python3
""" Module 2-measure_runtime.py"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n
start_time: float = time.time()


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time for wait_n(n, max_delay)
    Args:
        n (int): measure time argument
        max_delay (int): measure time argument
    Return:
        float: delay time in float format
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time: float = time.time()
    delay = (stop_time - start_time) / n
    return delay
