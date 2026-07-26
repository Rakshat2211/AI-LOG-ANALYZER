from backend.parsers.docker_parser import DockerParser
from backend.schemas.parsed_log import ParsedLog


def test_parse_docker_log():

    """
    Docker parser should create
    a ParsedLog object.
    """

    parser = DockerParser()

    raw_log = (
        "Container started successfully"
    )

    parsed = parser.parse(raw_log)

    assert parsed is not None

    assert isinstance(
        parsed,
        ParsedLog,
    )

    assert parsed.source == "Docker"

    assert parsed.level == "INFO"

    assert parsed.message == (
        "Container started successfully"
    )


def test_parse_trims_whitespace():

    """
    Docker parser should strip
    leading and trailing whitespace.
    """

    parser = DockerParser()

    raw_log = (
        "   Hello Docker   "
    )

    parsed = parser.parse(raw_log)

    assert parsed.message == "Hello Docker"


def test_empty_message():

    """
    Empty Docker logs
    should still be parsed.
    """

    parser = DockerParser()

    parsed = parser.parse("")

    assert parsed is not None

    assert parsed.message == ""