#!/usr/bin/env python3
"""
    A type-annotated function to_kv that takes a string k and an int
    OR float v as arguments and returns a tuple. The first element
    of the tuple is the string k. The second element is the square
    of the int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string key and an int or float value into a tuple.

    Parameters:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string key
                           and the second element is the square of the int or
                           float value, annotated as a float.
    """
    return (k, v**2)
