#!/usr/bin/env python3
"""
    Annotate the below function’s parameters and return values
    with the appropriate types
"""
from typing import List, Tuple, Sequence, Iterable

vector = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> vector:
    """Return a list of tuples"""
    return [(i, len(i)) for i in lst]
