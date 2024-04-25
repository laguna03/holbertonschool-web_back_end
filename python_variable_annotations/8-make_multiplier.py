#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""

    def multiply(n: float):
        """Multiply n by multiplier."""
        return n * multiplier
    return multiply
