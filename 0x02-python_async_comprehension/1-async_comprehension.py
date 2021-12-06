#!/usr/bin/env python3
""" Module that  loop 10 times """

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Function that loops 10 times the async_generator function """
    return [number async for number in async_generator()]
