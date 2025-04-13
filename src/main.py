"""main.py"""

from src.settings import config
from src.utils import init_logger

logger = init_logger()


def main() -> None:
    """Run the main application."""
    logger.info("env: %s", config.env)
    logger.info("Hello, World!")


if __name__ == "__main__":
    main()
