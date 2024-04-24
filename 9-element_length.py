#!/usr/bin/env python3
"""
element_length - takes a list element as argument and returns the length of the element
"""

from typing import Sequence, Union, Any
from typing import List, Tuple


def element_length(lst: Sequence[Union[int, str, Tuple[Any], List[Any]]]) -> List[int]:
    """
    element_length - takes a list element as argument and returns the length of the element
    lst: list of integers, strings, tuples, and lists
    returns: list of integers representing the length of each element in lst
    """
    return [len(i) for i in lst]
