"""settings.py"""

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict


class Config(BaseModel):
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
