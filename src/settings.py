"""settings.py"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Config

    Attributes:
        env: (local, dev, prod)
        log_level: logging level
    """

    model_config = SettingsConfigDict(env_file=".env")

    # COMMON ENV
    env: str = Field(default="local")

    # logging
    log_level: str = Field(default="INFO")


config = Config()
