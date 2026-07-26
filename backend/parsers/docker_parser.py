from datetime import datetime

from backend.core.logger import logger
from backend.parsers.base import BaseParser
from backend.schemas.parsed_log import ParsedLog


class DockerParser(BaseParser):

    def parse(self, raw_log: str):

        try:

            return ParsedLog(

                timestamp=datetime.now(),

                source="Docker",

                level="INFO",

                message=raw_log.strip(),

            )

        except Exception as error:

            logger.error(
                "Failed to parse Docker log '{}': {}",
                raw_log,
                error,
            )

            return None