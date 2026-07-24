from fastapi import FastAPI

from backend.api.routes import router
from backend.core.config import settings
from backend.core.logger import logger
from backend.db.base import Base
from backend.db.database import engine
from backend.api.logs import router as log_router
from backend.api.collectors import router as collector_router
from backend.api.analysis import router as analysis_router
from backend.scheduler.collector_scheduler import CollectorScheduler

# Import models so SQLAlchemy knows about them
from backend.db.models import Log

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION,

    description="AI Powered Intelligent Log Analysis Platform"

)

app.include_router(router)

app.include_router(log_router)

app.include_router(collector_router)

app.include_router(analysis_router)

collector_scheduler = CollectorScheduler(interval=settings.COLLECTOR_INTERVAL)

@app.on_event("startup")
async def startup():

    Base.metadata.create_all(bind=engine)

    logger.info("Database tables created.")

    collector_scheduler.start()

    logger.info("Application Started")


@app.on_event("shutdown")
async def shutdown():

    collector_scheduler.stop()
    logger.info("Application Stopped")