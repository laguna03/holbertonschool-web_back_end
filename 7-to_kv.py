#!/usr/bin/python3
"""
to_kv - takes a string k and an int OR float v as arguments and returns a tuple
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv - takes a string k and an int OR float v as arguments and returns a tuple
    k: string
    v: int or float
    returns: tuple containing k and the square of v
    """
    return (k, v**2)
