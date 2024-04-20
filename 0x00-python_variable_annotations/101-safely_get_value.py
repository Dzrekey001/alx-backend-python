#!/bin/usr/env python3
"""
    Given the parameters and the return values,
    add type annotations to the function
"""
from typing import TypeVar, Dict, Union, Mapping, Any

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Parameters:
        dct (Dict[T, value]): The dictionary to retrieve the value from.
        key (T): The key to look up in the dictionary.
        default (value, optional): The default value to return if the
        key is not found. Defaults to None.

    Returns:
        value: The value corresponding to the key in the dictionary,
        or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
