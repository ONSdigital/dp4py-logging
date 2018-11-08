"""
Implements a custom logger with TRACE support
"""
from logging import getLoggerClass, addLevelName, setLoggerClass, NOTSET

TRACE = 5


class DPLogger(getLoggerClass()):
    def __init__(self, name, level=NOTSET):
        super().__init__(name, level)

        addLevelName(TRACE, "TRACE")

    def trace(self, msg, *args, **kwargs):
        if self.isEnabledFor(TRACE):
            self._log(TRACE, msg, args, **kwargs)