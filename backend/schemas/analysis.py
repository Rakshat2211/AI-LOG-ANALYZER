from pydantic import BaseModel

from .log import LogResponse


class AnalysisResponse(BaseModel):
    """
    Response returned by the Analysis API.

    For now, it simply returns the logs that will be
    analyzed in future milestones.
    """

    total_logs: int
    logs: list[LogResponse]