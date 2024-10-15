#!/usr/bin/env python3
""" Module 3-tasks.py """
import asyncio
from typing import Optional

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Optional[asyncio.Task]:
    """
    Takes the integer max_delay and returns a task
    Args:
        max_delay (int): maximum delay time limit
    Return:
        asyncio.Task: asynchrounous function
    """
    return asyncio.create_task(wait_random(max_delay))
