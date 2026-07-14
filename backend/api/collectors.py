from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.collectors.manager import CollectorManager
from backend.db.database import get_db

router = APIRouter(
    prefix="/collectors",
    tags=["Collectors"]
)


@router.post("/run")
def run_collectors(
    db: Session = Depends(get_db),
):

    manager = CollectorManager(db)

    count = manager.collect_all_logs()

    return {
        "message": f"{count} logs collected successfully."
    }