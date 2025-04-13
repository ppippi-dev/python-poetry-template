"""utils.py"""

import logging

from rich.console import Console
from rich.logging import RichHandler

from src.settings import config


def init_logger() -> logging.Logger:
    """Initialize the Python logger.

    Returns:
        logging.Logger: Initialized logger

    """
    logging.basicConfig(
        level=config.log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, console=Console(width=127))],
    )

    log = logging.getLogger("rich")

    return log
