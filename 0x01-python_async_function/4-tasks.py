#!/usr/bin/env python3
""" Module 4-tasks.py"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n spawns wait_random n times with the specified max_delay
    Args:
        n (int): number of times to spawn wait_delay()
        max_delay (int): max number limit of delay
    Return:
        delay [float]: Actual random delay generate
    """
    tasks = [task_wait_random(max_delay) for x in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
