from datetime import datetime

from backend.schemas.log import LogResponse
from backend.services.anomaly_service import detect_anomalies


def create_log(

    level: str,

    message: str = "Message",

    source: str = "Dummy",

):

    return LogResponse(

        id=1,

        timestamp=datetime.now(),

        source=source,

        level=level,

        message=message,

        created_at=datetime.now(),
    )


def test_empty_logs():

    anomalies = detect_anomalies([])

    assert anomalies == []


def test_high_error_rate():

    logs = [

        create_log("ERROR"),

        create_log("ERROR"),

        create_log("INFO"),

        create_log("INFO"),

    ]

    anomalies = detect_anomalies(logs)

    assert "High error rate detected." in anomalies


def test_high_warning_rate():

    logs = [

        create_log("WARNING"),

        create_log("WARNING"),

        create_log("WARNING"),

        create_log("WARNING"),

        create_log("INFO"),

    ]

    anomalies = detect_anomalies(logs)

    assert "Large number of warning logs detected." in anomalies


def test_repeated_messages():

    logs = [

        create_log(

            "INFO",

            message="Connection Failed",

        )

        for _ in range(5)

    ]

    anomalies = detect_anomalies(logs)

    assert any(

        "Repeated log message detected"

        in anomaly

        for anomaly in anomalies

    )


def test_source_dominance():

    logs = [

        create_log(

            "INFO",

            source="Docker",

        )

        for _ in range(8)

    ]

    logs.append(

        create_log(

            "INFO",

            source="Dummy",

        )

    )

    anomalies = detect_anomalies(logs)

    assert any(

        "Docker"

        in anomaly

        for anomaly in anomalies

    )


def test_healthy_system():

    logs = [

        create_log("INFO"),

        create_log("INFO"),

        create_log("WARNING"),

    ]

    anomalies = detect_anomalies(logs)

    assert "No error logs detected." in anomalies