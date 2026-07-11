from fastapi import APIRouter

from backend.core.config import settings

router = APIRouter()


@router.get("/")
def root():

    return {

        "message": "Welcome to Intelligent Log Analyzer API"

    }


@router.get("/health")
def health():

    return {

        "status": "healthy",

        "application": settings.APP_NAME,

        "version": settings.APP_VERSION,

        "environment": settings.ENVIRONMENT,

    }