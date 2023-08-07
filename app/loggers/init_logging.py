"""Initializes the loggers"""

import logging
import sys
import os

from app.config import LOGS_DIR


def init_logging() -> None:
    """Initializes the loggers"""

    kwargs = {
        "level": os.getenv("LOGGER_LEVEL", "INFO"),
        "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        "datefmt": "%Y-%m-%d %H:%M:%S",
    }

    if os.getenv("FILE_LOGGING_ENABLED", "False").lower() == "true":
        os.makedirs(LOGS_DIR, exist_ok=True)
        kwargs["filename"] = LOGS_DIR.joinpath("app.log")
        kwargs["filemode"] = "w"
    else:
        kwargs["stream"] = sys.stdout

    logging.basicConfig(**kwargs)

    logging.getLogger("core").debug("Logging was initiated.")
