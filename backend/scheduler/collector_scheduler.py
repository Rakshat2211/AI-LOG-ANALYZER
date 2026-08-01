import threading

from backend.collectors.manager import CollectorManager
from backend.core.logger import logger
from backend.db.database import SessionLocal


class CollectorScheduler:
    """
    Runs the collector manager periodically
    in a background thread.
    """

    def __init__(self, interval: int = 1800):

        self.interval = interval

        self._running = False

        self._thread = None

        # Signals the thread to stop immediately.
        self._stop_event = threading.Event()

        # Ensures only one collection runs at a time.
        self._collection_lock = threading.Lock()

    def _run(self):

        logger.info("Collector scheduler started.")

        while self._running:

            # Prevent overlapping executions.
            if not self._collection_lock.acquire(blocking=False):

                logger.warning(
                    "Previous collection is still running. Skipping this cycle."
                )

            else:

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

                    self._collection_lock.release()

            # Wait until interval expires or stop() wakes us.
            if self._stop_event.wait(self.interval):
                break

        logger.info("Collector scheduler thread exited.")

    def start(self):

        if self._running:

            logger.warning(
                "Collector scheduler is already running."
            )

            return

        self._running = True

        self._stop_event.clear()

        self._thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="CollectorScheduler",
        )

        self._thread.start()

        logger.info(
            "Collector scheduler thread created."
        )

    def stop(self):

        if not self._running:
            return

        logger.info(
            "Stopping collector scheduler..."
        )

        self._running = False

        self._stop_event.set()

        if self._thread is not None:

            self._thread.join(timeout=5)

        logger.info(
            "Collector scheduler stopped."
        )