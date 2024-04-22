#!/usr/bin/env python3
"""asyncio task"""
from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task for the wait_random coroutine
        with the specified max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
