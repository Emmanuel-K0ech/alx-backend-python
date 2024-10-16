#!/usr/bin/env python3
""" Module 2-async_comprehension.py """
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Returns random numbers receive from an asynchrounous generator
    """
    result = []
    async for res in aiter(async_generator()):
        result.append(res)
    return result
