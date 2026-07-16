from datetime import datetime

from backend.core.logger import logger
from backend.parsers.base import BaseParser


class DockerParser(BaseParser):

    def parse(self, raw_log: str):

        try:

            return {

                "timestamp": datetime.now(),

                "source": "Docker",

                "level": "INFO",

                "message": raw_log.strip(),

            }

        except Exception as error:

            logger.error(
                "Failed to parse Docker log '%s': %s",
                raw_log,
                error,
            )

            return None