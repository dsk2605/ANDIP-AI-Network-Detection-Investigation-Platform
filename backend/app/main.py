import asyncio
from contextlib import asynccontextmanager
from threading import Thread

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.v1.endpoints.alerts import router as alert_router
from app.api.v1.endpoints.analytics import router as analytics_router
from app.api.v1.endpoints.assets import router as asset_router
from app.api.v1.endpoints.dashboard import router as dashboard_router
from app.api.v1.endpoints.discovery import router as discovery_router
from app.collector.capture_service import PacketCaptureService
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import get_logger
from app.database.base import Base
from app.database.models import *
from app.database.session import engine
from app.middleware.logging_middleware import log_requests
from app.middleware.security_headers import security_headers
from app.websocket.event_worker import event_worker
from app.websocket.router import router as websocket_router

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "Starting %s v%s...",
        settings.APP_NAME,
        settings.APP_VERSION,
    )

    # ---------------------------------------
    # Start WebSocket Event Worker
    # ---------------------------------------

    websocket_task = asyncio.create_task(
        event_worker.start()
    )

    # ---------------------------------------
    # Start Packet Capture
    # ---------------------------------------

    packet_capture_service = PacketCaptureService()

    capture_thread = Thread(
        target=packet_capture_service.start,
        daemon=True,
        name="PacketCaptureThread",
    )

    capture_thread.start()

    logger.info(
        "Packet Capture Service started successfully."
    )

    yield

    logger.info(
        "Shutting down %s...",
        settings.APP_NAME,
    )

    websocket_task.cancel()

    try:
        await websocket_task
    except asyncio.CancelledError:
        logger.info(
            "WebSocket Event Worker stopped."
        )


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# --------------------------------------------------
# Exception Handlers
# --------------------------------------------------

register_exception_handlers(app)

# --------------------------------------------------
# Middleware
# --------------------------------------------------

app.middleware("http")(log_requests)
app.middleware("http")(security_headers)

# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Database
# --------------------------------------------------

Base.metadata.create_all(bind=engine)

# --------------------------------------------------
# Root
# --------------------------------------------------


@app.get("/")
async def root():

    logger.info("Root endpoint accessed.")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


# --------------------------------------------------
# Health
# --------------------------------------------------


@app.get("/health")
async def health():

    try:

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        logger.info("Health check passed.")

        return {
            "status": "healthy",
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "database": "connected",
            "collector": "running",
            "detection_engine": "running",
            "alerts": "ready",
            "websocket": "running",
        }

    except Exception:

        logger.exception("Health check failed.")

        return {
            "status": "unhealthy",
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "database": "disconnected",
        }


# --------------------------------------------------
# API Routers
# --------------------------------------------------

app.include_router(asset_router)
app.include_router(discovery_router)
app.include_router(alert_router)
app.include_router(dashboard_router)
app.include_router(analytics_router)

# WebSocket
app.include_router(websocket_router)