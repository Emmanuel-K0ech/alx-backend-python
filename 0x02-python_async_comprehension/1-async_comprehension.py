#!/usr/bin/env python3
""" Module 2-async_comprehension.py """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns random numbers receive from an asynchrounous generator
    """
    result: List[float] = []
    async for res in aiter(async_generator()):
        result.append(res)
    return result
