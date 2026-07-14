from sqlalchemy.orm import Session

from backend.collectors.implementations.dummy import DummyCollector
from backend.schemas.log import LogCreate
from backend.services.log_service import create_log


class CollectorManager:

    def __init__(self, db: Session):

        self.db = db

        self.collectors = [
            DummyCollector(),
        ]

    def collect_all_logs(self):

        total_logs = 0

        for collector in self.collectors:

            logs = collector.collect()

            for log in logs:

                log_schema = LogCreate(
                    timestamp=log["timestamp"],
                    source=log["source"],
                    level=log["level"],
                    message=log["message"],
                )

                create_log(
                    self.db,
                    log_schema,
                )

                total_logs += 1

        return total_logs