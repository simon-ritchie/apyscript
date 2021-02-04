"""Definitions and interface for loggers.
"""

import logging
from logging import INFO
from logging import getLogger, Logger, Formatter, StreamHandler


_LOGGER_NAME_USER_INFO: str = 'user_info'


def get_user_info_logger() -> Logger:
    """
    Get information logger used when user is manipulating
    (e.g., export command).

    Returns
    -------
    logger : Logger
        Information logger as following settings.
        - Level: INFO
        - Format: `%Y-%m-%d %H:%M:%S. <message>`
    """
    logger: Logger = getLogger(_LOGGER_NAME_USER_INFO)
    logger.setLevel(level=INFO)

    stream_handler: StreamHandler = StreamHandler()
    formatter: Formatter = Formatter(
        fmt='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler.setFormatter(fmt=formatter)
    logger.addHandler(stream_handler)
    return logger

