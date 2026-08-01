from sqlalchemy.orm import Session

from backend.schemas.analysis import (
    AnalysisResponse,
    AIAnalysisResponse,
)
from backend.schemas.log import LogResponse

from backend.services.log_service import get_logs
from backend.services.statistics_service import generate_statistics
from backend.services.anomaly_service import detect_anomalies
from backend.services.context_builder import build_analysis_context
from backend.services.llm_service import generate_ai_analysis


def prepare_analysis_data(
    db: Session,
):
    """
    Prepare all analysis data that is common
    between dashboard analytics and AI analysis.
    """

    logs = get_logs(db)

    response_logs = [
        LogResponse.model_validate(log)
        for log in logs
    ]

    statistics = generate_statistics(response_logs)

    anomalies = detect_anomalies(response_logs)

    analysis_context = build_analysis_context(
        total_logs=statistics.total_logs,
        info_logs=statistics.info_logs,
        warning_logs=statistics.warning_logs,
        error_logs=statistics.error_logs,
        logs_by_source=statistics.logs_by_source,
        most_common_level=statistics.most_common_level,
        anomalies=anomalies,
    )

    return {
        "logs": response_logs,
        "statistics": statistics,
        "anomalies": anomalies,
        "analysis_context": analysis_context,
    }


def get_logs_for_analysis(
    db: Session,
):
    """
    Fast endpoint.
    Returns dashboard data without AI generation.
    """

    analysis_data = prepare_analysis_data(db)

    statistics = analysis_data["statistics"]

    return AnalysisResponse(

        total_logs=statistics.total_logs,

        info_logs=statistics.info_logs,

        warning_logs=statistics.warning_logs,

        error_logs=statistics.error_logs,

        logs_by_source=statistics.logs_by_source,

        most_common_level=statistics.most_common_level,

        anomalies=analysis_data["anomalies"],

        analysis_context=analysis_data["analysis_context"],

        # AI will be fetched separately
        ai_summary="",

        logs=analysis_data["logs"],
    )


def get_ai_analysis(
    db: Session,
):
    """
    Slow endpoint.
    Generates AI summary only.
    """

    analysis_data = prepare_analysis_data(db)

    ai_summary = generate_ai_analysis(
        analysis_data["analysis_context"]
    )

    return AIAnalysisResponse(
        ai_summary=ai_summary,
    )