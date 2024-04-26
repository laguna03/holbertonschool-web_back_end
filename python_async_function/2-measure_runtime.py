#!/usr/bin/env python3
"""Measure runtime"""

import asyncio
import random
import time
from typing import List


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start
