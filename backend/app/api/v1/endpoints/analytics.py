from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.analytics_service import AnalyticsService
from app.schemas.analytics import AnalyticsResponse

from app.schemas.asset import AssetResponse

from app.schemas.recommendation import (
    SecurityRecommendation,
)

from app.schemas.discovery_summary import (
    DiscoverySummaryResponse,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/overview",
    response_model=AnalyticsResponse,
)
def get_analytics(
    db: Session = Depends(get_db),
):
    service = AnalyticsService(db)
    return service.get_overview()


@router.get(
    "/top-risk-assets",
    response_model=list[AssetResponse],
)
def get_top_risk_assets(
    db: Session = Depends(get_db),
):
    service = AnalyticsService(db)
    return service.get_top_risk_assets()


@router.get("/os-distribution")
def get_os_distribution(
    db: Session = Depends(get_db),
):
    service = AnalyticsService(db)
    return service.get_os_distribution()


@router.get("/environment-distribution")
def get_environment_distribution(
    db: Session = Depends(get_db),
):
    service = AnalyticsService(db)
    return service.get_environment_distribution()


@router.get("/asset-type-distribution")
def get_asset_type_distribution(
    db: Session = Depends(get_db),
):
    service = AnalyticsService(db)
    return service.get_asset_type_distribution()


@router.get(
    "/security-recommendations",
    response_model=list[SecurityRecommendation],
)
def get_security_recommendations(
    db: Session = Depends(get_db),
):
    service = AnalyticsService(db)
    return service.get_security_recommendations()


@router.get(
    "/discovery-summary",
    response_model=DiscoverySummaryResponse,
)
def get_discovery_summary(
    db: Session = Depends(get_db),
):
    service = AnalyticsService(db)
    return service.get_discovery_summary()