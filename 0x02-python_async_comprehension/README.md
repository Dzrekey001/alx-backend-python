# 0x02. Python - Async Comprehension

## Project Overview

In this project, we explore asynchronous generators and comprehension in Python. By the end of this project, you should be able to:

- Write an asynchronous generator
- Utilize async comprehensions
- Type-annotate generators

## Tasks

### Task 0: Async Generator

Write a coroutine called `async_generator` that loops 10 times, each time asynchronously waits for 1 second, then yields a random number between 0 and 10.

### Task 1: Async Comprehensions

Write a coroutine called `async_comprehension` that collects 10 random numbers using async comprehension over `async_generator`, then returns the 10 random numbers.

### Task 2: Run Time for Four Parallel Comprehensions

Write a `measure_runtime` coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it.

This project provides an opportunity to explore advanced asynchronous programming concepts in Python, enabling you to develop more efficient and responsive applications.
