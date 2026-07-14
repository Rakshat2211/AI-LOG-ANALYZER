from datetime import datetime

from backend.parsers.base import BaseParser


class DummyParser(BaseParser):

    def parse(self, raw_log):

        parts = raw_log.split("|")

        return {

            "timestamp": datetime.strptime(
                parts[0],
                "%Y-%m-%d %H:%M:%S"
            ),

            "source": parts[1],

            "level": parts[2],

            "message": parts[3],

        }