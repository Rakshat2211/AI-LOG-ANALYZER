from datetime import datetime

from pydantic import BaseModel


class LogCreate(BaseModel):

    timestamp: datetime

    source: str

    level: str

    message: str


class LogResponse(BaseModel):

    id: int

    timestamp: datetime

    source: str

    level: str

    message: str

    created_at: datetime

    class Config:

        from_attributes = True