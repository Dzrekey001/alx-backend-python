#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with
    the specified max_delay:

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of all delays (float values) in ascending order.
    """

    tasks = [wait_random(i) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
