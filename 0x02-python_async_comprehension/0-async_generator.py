#!/usr/bin/env python3
""" Module that  loop 10 times """


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ function that loop 10 times and yield a random """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
