from datetime import datetime
from backend.core.logger import logger
from backend.parsers.base import BaseParser


class DummyParser(BaseParser):

    def parse(self, raw_log):

        try:

            parts = raw_log.split("|")

            if len(parts) != 4:

                raise ValueError(
                    "Invalid log format."
                )

            return {

                "timestamp": datetime.strptime(
                    parts[0],
                    "%Y-%m-%d %H:%M:%S",
                ),

                "source": parts[1],

                "level": parts[2],

                "message": parts[3],

            }

        except Exception as error:

            logger.error(
                "Failed to parse log '%s': %s",
                raw_log,
                error,
            )

            return None