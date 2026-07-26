from unittest.mock import MagicMock

from backend.collectors.manager import CollectorManager

from backend.schemas.parsed_log import ParsedLog

from datetime import datetime


def create_parsed_log():

    return ParsedLog(

        timestamp=datetime.now(),

        source="Dummy",

        level="INFO",

        message="Application Started",
    )


def test_collect_all_logs(db):

    manager = CollectorManager(db)

    fake_collector = MagicMock()

    fake_collector.collect.return_value = [

        create_parsed_log(),

        create_parsed_log(),

    ]

    manager.collectors = [

        fake_collector,

    ]

    total = manager.collect_all_logs()

    assert total == 2


def test_collector_failure(db):

    manager = CollectorManager(db)

    failing = MagicMock()

    failing.collect.side_effect = Exception(
        "Failure"
    )

    manager.collectors = [

        failing,

    ]

    total = manager.collect_all_logs()

    assert total == 0


def test_multiple_collectors(db):

    manager = CollectorManager(db)

    collector_one = MagicMock()

    collector_two = MagicMock()

    collector_one.collect.return_value = [

        create_parsed_log()

    ]

    collector_two.collect.return_value = [

        create_parsed_log(),

        create_parsed_log(),

    ]

    manager.collectors = [

        collector_one,

        collector_two,

    ]

    total = manager.collect_all_logs()

    assert total == 3