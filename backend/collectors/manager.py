from sqlalchemy.orm import Session

from backend.collectors.implementations.dummy import DummyCollector
from backend.collectors.implementations.docker import DockerCollector
from backend.services.log_service import create_log


class CollectorManager:

    def __init__(self, db: Session):

        self.db = db

        self.collectors = [
            DummyCollector(),
            DockerCollector(),
        ]

    def collect_all_logs(self):

        total_logs = 0

        for collector in self.collectors:

            try:

                logs = collector.collect()

                for log in logs:

                    create_log(
                        self.db,
                        log,
                    )

                    total_logs += 1

            except Exception as error:

                from backend.core.logger import logger

                logger.exception(
                    "%s collector failed: %s",
                    collector.__class__.__name__,
                    error,
                )

                continue

        return total_logs