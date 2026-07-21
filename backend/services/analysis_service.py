from collections import Counter

from sqlalchemy.orm import Session

from backend.schemas.analysis import AnalysisResponse
from backend.schemas.log import LogResponse
from backend.services.log_service import get_logs
from backend.services.anomaly_service import detect_anomalies
from backend.services.context_builder import build_analysis_context


def get_logs_for_analysis(
    db: Session,
):
    # Step 1: Fetch logs
    logs = get_logs(db)

    # Step 2: Convert SQLAlchemy models to Pydantic models
    response_logs = [
        LogResponse.model_validate(log)
        for log in logs
    ]

    # Step 3: Generate statistics
    level_counter = Counter(
        log.level
        for log in response_logs
    )

    source_counter = Counter(
        log.source
        for log in response_logs
    )

    # Step 4: Detect anomalies
    anomalies = detect_anomalies(response_logs)

    # Step 5: Build AI context
    analysis_context = build_analysis_context(
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

        anomalies=anomalies,
    )

    # Step 6: Return API response
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

        anomalies=anomalies,

        analysis_context=analysis_context,

        logs=response_logs,
    )