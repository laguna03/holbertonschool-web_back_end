#!/usr/bin/env python3
"""
Function that takes a list of floats as argument and returns their sum as a float in type-annotated form
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Function that takes a list of floats as argument and returns their sum as a float in type-annotated form
    """
    return sum(input_list)
