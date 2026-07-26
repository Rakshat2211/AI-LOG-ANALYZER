from datetime import datetime

from backend.schemas.log import LogResponse
from backend.services.statistics_service import generate_statistics


def create_log(level: str, source: str = "Dummy"):

    return LogResponse(

        id=1,

        timestamp=datetime.now(),

        source=source,

        level=level,

        message="Test Message",

        created_at=datetime.now(),
    )


def test_empty_logs():

    stats = generate_statistics([])

    assert stats.total_logs == 0
    assert stats.info_logs == 0
    assert stats.warning_logs == 0
    assert stats.error_logs == 0
    assert stats.logs_by_source == {}
    assert stats.most_common_level is None


def test_statistics_counts():

    logs = [

        create_log("INFO"),

        create_log("INFO"),

        create_log("WARNING"),

        create_log("ERROR"),

    ]

    stats = generate_statistics(logs)

    assert stats.total_logs == 4
    assert stats.info_logs == 2
    assert stats.warning_logs == 1
    assert stats.error_logs == 1
    assert stats.most_common_level == "INFO"


def test_logs_by_source():

    logs = [

        create_log("INFO", "Docker"),

        create_log("ERROR", "Docker"),

        create_log("INFO", "Dummy"),

    ]

    stats = generate_statistics(logs)

    assert stats.logs_by_source == {

        "Docker": 2,

        "Dummy": 1,

    }


def test_only_error_logs():

    logs = [

        create_log("ERROR"),

        create_log("ERROR"),

        create_log("ERROR"),

    ]

    stats = generate_statistics(logs)

    assert stats.total_logs == 3
    assert stats.error_logs == 3
    assert stats.info_logs == 0
    assert stats.warning_logs == 0
    assert stats.most_common_level == "ERROR"