"""
Adds decorator to log execution times
"""
import logging

from inspect import isawaitable
from time import time


def timeit(method):
    async def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        if isawaitable(result):
            result = await result
        te = time()
        logging.info("Recorded execution time", extra={
            "method": {
                "name": method.__name__,
                "module": method.__module__
            },
            "time(ms)": (te - ts) * 1000
        })
        return result
    return timed
