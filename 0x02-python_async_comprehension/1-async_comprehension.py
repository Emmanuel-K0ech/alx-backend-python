#!/usr/bin/env python3
""" Module 2-async_comprehension.py """
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns random numbers receive from an asynchrounous generator
    """
    return [numb async for numb in async_generator()]
