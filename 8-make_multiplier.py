#!/usr/bin/python3
"""
make_multiplier - takes a float multiplier as argument and returns a function that multiplies a float by multiplier
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier - takes a float multiplier as argument and returns a function that multiplies a float by multiplier
    multiplier: float
    returns: function that multiplies a float by multiplier
    """
    def multiply(n: float) -> float:
        """
        multiply - takes a float n as argument and returns the product of n and multiplier
        n: float
        returns: product of n and multiplier
        """
        return n * multiplier
    return multiply
