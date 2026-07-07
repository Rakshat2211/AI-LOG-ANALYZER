from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():

    return {
        "message": "Welcome to Intelligent Log Analyzer API"
    }


@router.get("/health")
def health():

    return {
        "status":"healthy",

        "application":"Intelligent Log Analyzer",

        "version":"1.0.0",

        "environment":"development"
    }