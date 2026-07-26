from datetime import datetime

from backend.parsers.dummy_parser import DummyParser
from backend.schemas.parsed_log import ParsedLog


def test_parse_valid_log():

    """
    Parser should correctly normalize
    a valid dummy log.
    """

    parser = DummyParser()

    raw_log = (
        "2026-07-25 10:30:45"
        "|Dummy"
        "|INFO"
        "|Application Started"
    )

    parsed = parser.parse(raw_log)

    assert parsed is not None

    assert isinstance(
        parsed,
        ParsedLog,
    )

    assert parsed.timestamp == datetime(
        2026,
        7,
        25,
        10,
        30,
        45,
    )

    assert parsed.source == "Dummy"

    assert parsed.level == "INFO"

    assert parsed.message == "Application Started"


def test_parse_invalid_log():

    """
    Invalid log format
    should return None.
    """

    parser = DummyParser()

    raw_log = "Invalid Log"

    parsed = parser.parse(raw_log)

    assert parsed is None


def test_parse_missing_fields():

    """
    Missing fields
    should return None.
    """

    parser = DummyParser()

    raw_log = (
        "2026-07-25 10:30:45"
        "|Dummy"
        "|INFO"
    )

    parsed = parser.parse(raw_log)

    assert parsed is None