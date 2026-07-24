from datetime import datetime

from pydantic import BaseModel


class ParsedLog(BaseModel):
    """
    Represents a normalized log produced
    by any parser.
    """

    timestamp: datetime

    source: str

    level: str

    message: str