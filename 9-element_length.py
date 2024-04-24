#!/usr/bin/env python3
"""
module to return the length of elements in a list
"""

from typing import Sequence, Union, Any
from typing import List, Tuple


def element_length(lst: Sequence[Union[int, str, Tuple[Any], List[Any]]]) -> List[int]:
    """
    element_length - takes a list element as argument and returns the length of the element
    """
    return [len(i) for i in lst]
