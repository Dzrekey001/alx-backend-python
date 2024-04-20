#!/usr/bin/env python3
"""
    A type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that mutiple 'multiplier' by n"""

    def mlp(n: float) -> float:
        return multiplier * n

    return mlp
