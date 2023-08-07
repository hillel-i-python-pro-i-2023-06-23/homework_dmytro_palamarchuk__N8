"""Logging getting"""

import logging


def get_core_logger() -> logging.Logger:
    """
    Get the core logger

    Returns
    -------
    logging.Logger
        the core logger
    """
    return logging.getLogger("core")


def get_custom_logger(logger_name: str) -> logging.Logger:
    """
    Get the custom logger

    Parameters
    ----------
    logger_name : str
        the name of the logger

    Returns
    -------
    logging.Logger
        the custom logger
    """
    return logging.getLogger(logger_name)
