from collections import Counter

from backend.schemas.log import LogResponse


def generate_statistics(
    logs: list[LogResponse],
) -> dict:
    """
    Generates statistical information from logs.
    """

    level_counter = Counter(
        log.level
        for log in logs
    )

    source_counter = Counter(
        log.source
        for log in logs
    )

    return {

        "total_logs": len(logs),

        "info_logs": level_counter.get("INFO", 0),

        "warning_logs": level_counter.get("WARNING", 0),

        "error_logs": level_counter.get("ERROR", 0),

        "logs_by_source": dict(source_counter),

        "most_common_level": (

            level_counter.most_common(1)[0][0]

            if level_counter

            else None

        ),
    }