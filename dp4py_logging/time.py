"""
Adds decorator to log execution times
"""
import logging

from inspect import isawaitable
from time import time

_is_debug = logging.getLogger().getEffectiveLevel() == logging.DEBUG


def timeit(method):
    async def timed(*args, **kw):
        if _is_debug:
            ts = time()
            result = method(*args, **kw)
            if isawaitable(result):
                result = await result
            te = time()
            logging.debug("Recorded execution time", extra={
                "method": {
                    "name": method.__name__,
                    "module": method.__module__
                },
                "time(ms)": (te - ts) * 1000
            })
            return result
        else:
            result = method(*args, **kw)
            if isawaitable(result):
                result = await result
            return result
    return timed
