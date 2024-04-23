#!/usr/bin/env python3
"""asyncio task"""
import random
import asyncio


async def async_generator() -> None:
    """
    Coroutine that loops 10 times, asynchronously waits for 1 second each time,
    then yields a random number between 0 and 10.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ range(10):
        await asncio.sleep(1)
        yield random.randint(0, 10)
