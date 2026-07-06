from fastapi import FastAPI

from backend.api.routes import router
from backend.core.config import settings
from backend.core.logger import logger

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION,

    description="AI Powered Intelligent Log Analysis Platform"

)

app.include_router(router)


@app.on_event("startup")
async def startup():

    logger.info("Application Started")


@app.on_event("shutdown")
async def shutdown():

    logger.info("Application Stopped")