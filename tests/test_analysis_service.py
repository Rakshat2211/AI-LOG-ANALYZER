from datetime import datetime
from unittest.mock import patch

from backend.schemas.log import LogResponse
from backend.services.analysis_service import (
    get_logs_for_analysis,
)


def create_log():

    return LogResponse(

        id=1,

        timestamp=datetime.now(),

        source="Dummy",

        level="INFO",

        message="Application Started",

        created_at=datetime.now(),
    )


@patch("backend.services.analysis_service.generate_ai_analysis")
@patch("backend.services.analysis_service.get_logs")
def test_analysis_pipeline(

    mock_get_logs,

    mock_generate_ai,

):

    mock_get_logs.return_value = [

        create_log(),

        create_log(),
    ]

    mock_generate_ai.return_value = "Everything looks healthy."

    response = get_logs_for_analysis(None)

    assert response.total_logs == 2

    assert response.info_logs == 2

    assert response.error_logs == 0

    assert response.ai_summary == "Everything looks healthy."

    assert len(response.logs) == 2