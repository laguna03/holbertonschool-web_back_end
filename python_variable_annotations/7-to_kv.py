#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int OR float v and returns a tuple."""
    return (k, v * v)
