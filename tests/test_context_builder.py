from backend.services.context_builder import (
    build_analysis_context,
)


def test_context_contains_statistics():

    context = build_analysis_context(

        total_logs=100,

        info_logs=60,

        warning_logs=25,

        error_logs=15,

        logs_by_source={
            "Docker": 70,
            "Dummy": 30,
        },

        most_common_level="INFO",

        anomalies=[],
    )

    assert "Total Logs: 100" in context

    assert "INFO Logs: 60" in context

    assert "WARNING Logs: 25" in context

    assert "ERROR Logs: 15" in context

    assert "Docker: 70" in context

    assert "Dummy: 30" in context

    assert "Most Common Log Level: INFO" in context


def test_context_contains_anomalies():

    context = build_analysis_context(

        total_logs=5,

        info_logs=2,

        warning_logs=1,

        error_logs=2,

        logs_by_source={
            "Dummy": 5,
        },

        most_common_level="ERROR",

        anomalies=[

            "High error rate detected.",

            "Repeated log message detected.",
        ],
    )

    assert "High error rate detected." in context

    assert "Repeated log message detected." in context


def test_context_no_anomalies():

    context = build_analysis_context(

        total_logs=10,

        info_logs=10,

        warning_logs=0,

        error_logs=0,

        logs_by_source={
            "Dummy": 10,
        },

        most_common_level="INFO",

        anomalies=[],
    )

    assert "Detected Anomalies:" in context

    assert "- None" in context