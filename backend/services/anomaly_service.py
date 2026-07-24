from collections import Counter

from backend.schemas.log import LogResponse


def detect_anomalies(
    logs: list[LogResponse],
) -> list[str]:

    anomalies = []

    if not logs:
        return anomalies

    total_logs = len(logs)

    # -------------------------
    # Count Log Levels
    # -------------------------

    level_counter = Counter(
        log.level
        for log in logs
    )

    source_counter = Counter(
        log.source
        for log in logs
    )

    message_counter = Counter(
        log.message
        for log in logs
    )

    # -------------------------
    # High Error Rate
    # -------------------------

    if level_counter["ERROR"] / total_logs > 0.20:

        anomalies.append(
            "High error rate detected."
        )

    # -------------------------
    # High Warning Rate
    # -------------------------

    if level_counter["WARNING"] / total_logs > 0.30:

        anomalies.append(
            "Large number of warning logs detected."
        )

    # -------------------------
    # Docker Dominance
    # -------------------------

    for source, count in source_counter.items():

        if count / total_logs > 0.70:

            anomalies.append(
                f"{source} is generating unusually high log volume."
            )

    # -------------------------
    # Repeated Errors
    # -------------------------

    for message, count in message_counter.items():

        if count >= 5:

            anomalies.append(
                f"Repeated log message detected ({count} occurrences): {message}"
            )

    # -------------------------
    # Healthy System
    # -------------------------

    if level_counter["ERROR"] == 0:

        anomalies.append(
            "No error logs detected."
        )

    return anomalies