from pydantic import BaseModel

from backend.schemas.log import LogResponse


class AnalysisResponse(BaseModel):
    total_logs: int

    info_logs: int

    warning_logs: int

    error_logs: int

    logs_by_source: dict[str, int]

    most_common_level: str | None

    anomalies: list[str]

    analysis_context: str

    logs: list[LogResponse]