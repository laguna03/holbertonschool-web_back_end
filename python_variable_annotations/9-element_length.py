#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of the lengths of the elements of lst."""
    return [(i, len(i)) for i in lst]
