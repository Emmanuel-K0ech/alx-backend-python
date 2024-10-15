#!/usr/bin/env python3
"""
Asynchoronous coroutine that takes in an integer argument
that waits for a random delay and eventually return it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a delay then returns it
    Args:
        max_delay (int): Max number of seconds
    Return:
        float: actual delay time in seconds.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
