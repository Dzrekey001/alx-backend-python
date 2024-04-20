#!/usr/bin/env python3
"""
Safely retrieves the first element of a sequence.

Parameters:
    lst (Sequence[Any]): The sequence from which to
    retrieve the first element.

Returns:
    Union[Any, None]: The first element of the sequence,
    or None if the sequence is empty.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns:
        Union[Any, None]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
