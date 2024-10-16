#!/usr/bin/env python3
""" Module 0.async_generator.py """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, each time asynchrounously wait 1 second
    then yield a random module
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
