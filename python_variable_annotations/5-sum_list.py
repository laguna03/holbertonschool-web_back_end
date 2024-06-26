#!/usr/bin/env python3
"""This module defines a function with type annotations."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of floats"""
    return sum(input_list)
