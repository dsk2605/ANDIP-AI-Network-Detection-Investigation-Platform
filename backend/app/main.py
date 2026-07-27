from fastapi import FastAPI
from sqlalchemy import text

from app.database.session import engine
from app.api.v1.endpoints.assets import router as asset_router

app = FastAPI(
    title="ANDIP API",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "product": "ANDIP",
        "status": "running"
    }


@app.get("/health")
async def health():

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "backend": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "backend": "healthy",
            "database": str(e)
        }

app.include_router(asset_router)