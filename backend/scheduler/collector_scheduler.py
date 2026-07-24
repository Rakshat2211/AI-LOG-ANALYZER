import threading
import time

from backend.collectors.manager import CollectorManager
from backend.core.logger import logger
from backend.db.database import SessionLocal


class CollectorScheduler:
    """
    Runs the collector manager
    periodically in a background thread.
    """

    def __init__(self, interval: int = 60):

        self.interval = interval

        self._running = False

        self._thread = None

    def _run(self):

        logger.info("Collector scheduler started.")

        while self._running:

            db = SessionLocal()

            try:

                logger.info(
                    "Running scheduled log collection..."
                )

                manager = CollectorManager(db)

                total_logs = manager.collect_all_logs()

                logger.info(
                    "Scheduled collection completed. {} logs collected.",
                    total_logs,
                )

            except Exception as error:

                logger.exception(
                    "Collector scheduler failed: {}",
                    error,
                )

            finally:

                db.close()

            time.sleep(self.interval)

    def start(self):

        if self._running:
            return

        self._running = True

        self._thread = threading.Thread(
            target=self._run,
            daemon=True,
        )

        self._thread.start()

    def stop(self):

        self._running = False

        logger.info(
            "Collector scheduler stopped."
        )