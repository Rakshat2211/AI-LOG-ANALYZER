from datetime import datetime

from backend.schemas.log import ParsedLog


def sample_parsed_log():

    """
    Returns a sample ParsedLog object
    for use in tests.
    """

    return ParsedLog(

        timestamp=datetime.now(),

        source="Dummy",

        level="INFO",

        message="Application Started",
    )


def sample_error_log():

    """
    Returns a ParsedLog representing
    an error log.
    """

    return ParsedLog(

        timestamp=datetime.now(),

        source="Dummy",

        level="ERROR",

        message="Payment Service Crashed",
    )