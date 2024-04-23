#!/usr/bin/env python3
"""Asyncio task"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns a list if awaited async function"""
    start_time = time.time()
    funcs = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*funcs)
    end_time = time.time()

    return end_time - start_time
