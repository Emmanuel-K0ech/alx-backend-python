#!/usr/bin/env python3
""" Module 0.async_generator.py """
import asyncio
import random


async def async_generator():
    """
    Loops 10 times, each time asynchrounously wait 1 second
    then yield a random module
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
