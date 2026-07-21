from collections import Counter

from backend.schemas.log import LogResponse


def detect_anomalies(
    logs: list[LogResponse],
) -> list[str]:
    """
    Detects simple anomalies in the log dataset.
    """

    anomalies = []

    if not logs:
        anomalies.append("No logs available.")

        return anomalies

    level_counter = Counter(
        log.level
        for log in logs
    )

    source_counter = Counter(
        log.source
        for log in logs
    )

    total_logs = len(logs)

    info = level_counter.get("INFO", 0)

    warning = level_counter.get("WARNING", 0)

    error = level_counter.get("ERROR", 0)

    # Rule 1
    if error > (info + warning):
        anomalies.append("High error rate detected.")

    # Rule 2
    for source, count in source_counter.items():

        if count / total_logs > 0.7:

            anomalies.append(
                f"{source} is generating unusually high log volume."
            )

    return anomalies