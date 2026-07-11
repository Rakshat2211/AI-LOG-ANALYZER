from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi import Depends

from backend.db.database import SessionLocal
from backend.schemas.log import (
    LogCreate,
    LogResponse,
)

from backend.services.log_service import (
    create_log,
    get_logs,
)

router = APIRouter(
    prefix="/logs",
    tags=["Logs"],
)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.post(
    "/",
    response_model=LogResponse,
)
def add_log(

    log: LogCreate,

    db: Session = Depends(get_db),

):

    return create_log(
        db,
        log,
    )


@router.get(
    "/",
    response_model=list[LogResponse],
)
def fetch_logs(

    db: Session = Depends(get_db),

):

    return get_logs(db)