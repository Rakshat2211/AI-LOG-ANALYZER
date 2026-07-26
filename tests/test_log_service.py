from datetime import datetime

from backend.services.log_service import (
    create_log,
    get_logs,
)

from backend.schemas.parsed_log import ParsedLog


def test_create_log(db):
    """
    Verify that a log is correctly
    persisted to the database.
    """

    parsed_log = ParsedLog(

        timestamp=datetime.now(),

        source="Dummy",

        level="INFO",

        message="Application Started",
    )

    saved_log = create_log(
        db,
        parsed_log,
    )

    assert saved_log.id is not None

    assert saved_log.source == "Dummy"

    assert saved_log.level == "INFO"

    assert saved_log.message == "Application Started"


def test_get_logs(db):
    """
    Verify all logs
    are returned.
    """

    create_log(

        db,

        ParsedLog(

            timestamp=datetime.now(),

            source="Dummy",

            level="INFO",

            message="One",
        ),
    )

    create_log(

        db,

        ParsedLog(

            timestamp=datetime.now(),

            source="Docker",

            level="ERROR",

            message="Two",
        ),
    )

    logs = get_logs(db)

    assert len(logs) == 2

    assert logs[0].message == "One"

    assert logs[1].message == "Two"


def test_empty_database(db):
    """
    Empty database
    should return empty list.
    """

    logs = get_logs(db)

    assert logs == []