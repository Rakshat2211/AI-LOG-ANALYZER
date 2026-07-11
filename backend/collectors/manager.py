from backend.collectors.implementations.dummy import DummyCollector


class CollectorManager:

    def __init__(self):

        self.collectors = [

            DummyCollector(),

        ]

    def collect_all_logs(self):

        logs = []

        for collector in self.collectors:

            logs.extend(

                collector.collect()

            )

        return logs