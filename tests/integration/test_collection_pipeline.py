from datetime import datetime
from unittest.mock import patch

from backend.schemas.log import LogResponse
from backend.services.analysis_service import (
    get_logs_for_analysis,
)


def create_log(
    level="INFO",
    source="Dummy",
    message="Application Started",
):

    return LogResponse(

        id=1,

        timestamp=datetime.now(),

        source=source,

        level=level,

        message=message,

        created_at=datetime.now(),
    )


@patch(
    "backend.services.analysis_service.generate_ai_analysis"
)
@patch(
    "backend.services.analysis_service.get_logs"
)
def test_complete_analysis_pipeline(

    mock_get_logs,

    mock_ai,

):

    logs = [

        create_log(),

        create_log(),

        create_log(
            level="ERROR",
            message="Database Failure",
        ),

    ]

    mock_get_logs.return_value = logs

    mock_ai.return_value = (
        "AI Analysis Complete"
    )

    response = get_logs_for_analysis(
        db=None,
    )

    assert response.total_logs == 3

    assert response.info_logs == 2

    assert response.error_logs == 1

    assert response.warning_logs == 0

    assert response.logs_by_source == {

        "Dummy": 3

    }

    assert response.most_common_level == "INFO"

    assert response.analysis_context != ""

    assert response.ai_summary == (
        "AI Analysis Complete"
    )

    assert len(response.logs) == 3