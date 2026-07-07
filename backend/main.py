from fastapi import FastAPI

from backend.api.routes import router
from backend.core.config import settings
from backend.core.logger import logger
from backend.db.base import Base
from backend.db.database import engine

# Import models so SQLAlchemy knows about them
from backend.db.models import Log

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION,

    description="AI Powered Intelligent Log Analysis Platform"

)

app.include_router(router)


@app.on_event("startup")
async def startup():

    Base.metadata.create_all(bind=engine)

    logger.info("Database tables created.")

    logger.info("Application Started")


@app.on_event("shutdown")
async def shutdown():

    logger.info("Application Stopped")