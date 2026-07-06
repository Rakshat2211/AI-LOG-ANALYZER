from functools import lru_cache
from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:

    def __init__(self):

        self.APP_NAME = os.getenv(
            "APP_NAME",
            "Intelligent Log Analyzer",
        )

        self.APP_VERSION = os.getenv(
            "APP_VERSION",
            "1.0.0",
        )

        self.ENVIRONMENT = os.getenv(
            "ENVIRONMENT",
            "development",
        )

        self.HOST = os.getenv(
            "HOST",
            "127.0.0.1",
        )

        self.PORT = int(
            os.getenv("PORT", "8000")
        )

        self.LOG_LEVEL = os.getenv(
            "LOG_LEVEL",
            "INFO",
        )


@lru_cache
def get_settings():

    return Settings()


settings = get_settings()