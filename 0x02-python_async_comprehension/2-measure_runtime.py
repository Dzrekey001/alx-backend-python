#!/usr/bin/env python3
"""Asyncio task"""
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """returns a list if awaited async function"""
    return await async_comprehension()
