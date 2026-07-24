from sqlalchemy.orm import Session

from backend.db.models.log import Log
from backend.schemas.log import LogCreate
from backend.schemas.parsed_log import ParsedLog


def create_log(
    db: Session,
    log: LogCreate | ParsedLog,
):

    db_log = Log(
        timestamp=log.timestamp,
        source=log.source,
        level=log.level,
        message=log.message,
    )

    db.add(db_log)

    db.commit()

    db.refresh(db_log)

    return db_log


def get_logs(
    db: Session,
):

    return db.query(Log).all()