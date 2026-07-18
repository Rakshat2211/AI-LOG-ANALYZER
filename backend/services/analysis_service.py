from sqlalchemy.orm import Session

from backend.schemas.analysis import AnalysisResponse
from backend.schemas.log import LogResponse
from backend.services.log_service import get_logs


def get_logs_for_analysis(
    db: Session,
):
    """
    Retrieves logs from the Log Service and prepares them
    for future analysis.
    """

    logs = get_logs(db)

    response_logs = [
        LogResponse.model_validate(log)
        for log in logs
    ]

    return AnalysisResponse(
        total_logs=len(response_logs),
        logs=response_logs,
    )