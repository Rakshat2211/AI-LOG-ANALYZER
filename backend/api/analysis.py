from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.schemas.analysis import AnalysisResponse
from backend.services.analysis_service import get_logs_for_analysis

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)


@router.get(
    "",
    response_model=AnalysisResponse,
)
def analyze_logs(
    db: Session = Depends(get_db),
):
    return get_logs_for_analysis(db)