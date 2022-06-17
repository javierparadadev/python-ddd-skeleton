import logging
from typing import Any

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.logger.Logger import Logger


class NativeConsoleLogger(BaseObject, Logger):

    _FORMAT = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self._FORMAT)
        self._logger.addHandler(console_handler)

    def debug(self, log: Any):
        self._logger.debug(log)

    def info(self, log: Any):
        self._logger.info(log)

    def error(self, log: Any):
        self._logger.error(log)

    def critical(self, log: Any):
        self._logger.critical(log)
