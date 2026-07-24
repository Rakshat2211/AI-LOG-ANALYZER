from pydantic import BaseModel


class StatisticsResponse(BaseModel):
    """
    Represents statistical information
    generated from collected logs.
    """

    total_logs: int

    info_logs: int

    warning_logs: int

    error_logs: int

    logs_by_source: dict[str, int]

    most_common_level: str | None