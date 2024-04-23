#!/usr/bin/env python3
"""asyncio task"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, asynchronously waits for 1 second each time,
    then yields a random number between 0 and 10.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
