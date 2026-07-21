from collections import Counter

from sqlalchemy.orm import Session

from backend.schemas.analysis import AnalysisResponse
from backend.schemas.log import LogResponse
from backend.services.log_service import get_logs


def get_logs_for_analysis(
    db: Session,
):
    logs = get_logs(db)

    response_logs = [
        LogResponse.model_validate(log)
        for log in logs
    ]

    level_counter = Counter(
        log.level
        for log in response_logs
    )

    source_counter = Counter(
        log.source
        for log in response_logs
    )

    return AnalysisResponse(
        total_logs=len(response_logs),

        info_logs=level_counter.get("INFO", 0),

        warning_logs=level_counter.get("WARNING", 0),

        error_logs=level_counter.get("ERROR", 0),

        logs_by_source=dict(source_counter),

        most_common_level=(
            level_counter.most_common(1)[0][0]
            if level_counter
            else None
        ),

        logs=response_logs,
    )