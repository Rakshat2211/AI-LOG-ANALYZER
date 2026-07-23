from sqlalchemy.orm import Session

from backend.schemas.analysis import AnalysisResponse
from backend.schemas.log import LogResponse

from backend.services.log_service import get_logs
from backend.services.statistics_service import generate_statistics
from backend.services.anomaly_service import detect_anomalies
from backend.services.context_builder import build_analysis_context
from backend.services.llm_service import generate_ai_analysis


def get_logs_for_analysis(
    db: Session,
):
    # Retrieve logs
    logs = get_logs(db)

    response_logs = [
        LogResponse.model_validate(log)
        for log in logs
    ]

    # Generate statistics
    statistics = generate_statistics(response_logs)

    # Detect anomalies
    anomalies = detect_anomalies(response_logs)

    # Build context
    analysis_context = build_analysis_context(

        total_logs=statistics["total_logs"],

        info_logs=statistics["info_logs"],

        warning_logs=statistics["warning_logs"],

        error_logs=statistics["error_logs"],

        logs_by_source=statistics["logs_by_source"],

        most_common_level=statistics["most_common_level"],

        anomalies=anomalies,
    )

    # Generate AI summary
    ai_summary = generate_ai_analysis(analysis_context)

    return AnalysisResponse(

        total_logs=statistics["total_logs"],

        info_logs=statistics["info_logs"],

        warning_logs=statistics["warning_logs"],

        error_logs=statistics["error_logs"],

        logs_by_source=statistics["logs_by_source"],

        most_common_level=statistics["most_common_level"],

        anomalies=anomalies,

        analysis_context=analysis_context,

        ai_summary=ai_summary,

        logs=response_logs,
    )