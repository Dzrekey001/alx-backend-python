#!/usr/bin/env python3
"""
    A type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


vector = List[Union[int, float]]


def sum_mixed_list(mxd_lst: vector) -> float:
    """Returns the sume of integers and floats"""
    return sum(mxd_lst)
