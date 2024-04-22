# 0x01. Python - Async

## Project Overview

This project focuses on asynchronous programming in Python, specifically utilizing the `async` and `await` syntax, `asyncio` library, and concurrent coroutines. By the end of this project, you should be able to:

- Explain `async` and `await` syntax
- Execute an async program with `asyncio`
- Run concurrent coroutines
- Create asyncio tasks
- Utilize the `random` module

## Task 0: The Basics of Async

Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (with a default value of 10) and returns a random delay between 0 and `max_delay` (inclusive) seconds.

Use the `random` module.

## Task 1: Let's Execute Multiple Coroutines at the Same Time with Async

Write an async routine `wait_n` that takes two integer arguments `n` and `max_delay`. Spawn `wait_random` `n` times with the specified `max_delay`.

`wait_n` should return the list of all delays (float values) in ascending order without using `sort()` due to concurrency.

## Task 2: Measure the Runtime

Import `wait_n` from the previous file (`1-concurrent_coroutines.py`). Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`.

Use the `time` module to measure an approximate elapsed time.

## Task 3: Tasks

Import `wait_random` from `0-basic_async_syntax.py`. Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

## Task 4: Tasks (Continued)

Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.


***
This project provides an opportunity to deepen your understanding of asynchronous programming in Python, enabling you to develop more efficient and responsive applications.
