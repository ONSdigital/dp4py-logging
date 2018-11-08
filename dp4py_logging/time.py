"""
Adds decorator to log execution times
"""
import os
import logging

from inspect import isawaitable
from time import time


def is_debug():
    try:
        level_is_debug = os.environ.get("LOG_LEVEL", "INFO").upper() == "DEBUG"
        return level_is_debug
    except Exception as e:
        logging.error("Error checking 'LOG_LEVEL'", exc_info=e)
        return False


_is_debug = is_debug()


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
