from datetime import datetime

from backend.collectors.base import BaseCollector
from backend.parsers.dummy_parser import DummyParser


class DummyCollector(BaseCollector):

    def __init__(self):

        self.parser = DummyParser()

    def collect(self):

        raw_logs = [

            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}|Dummy|INFO|Application Started",

            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}|Dummy|ERROR|Payment Service Crashed",

            f"THIS IS NOT A VALID LOG",

        ]

        parsed_logs = []

        for log in raw_logs:
            parsed = self.parser.parse(log)

            if parsed is not None:
                parsed_logs.append(parsed)

        return parsed_logs