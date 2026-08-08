from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.dashboard import (
    DashboardOverviewResponse,
    SeverityDistributionItem,
    ThreatTrendItem,
)
from app.services.dashboard_service import DashboardService
from app.schemas.alert import AlertResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/overview",
    response_model=DashboardOverviewResponse,
)
def get_dashboard_overview(
    db: Session = Depends(get_db),
):
    service = DashboardService(db)
    return service.get_overview()


@router.get(
    "/severity-distribution",
    response_model=list[SeverityDistributionItem],
)
def get_severity_distribution(
    db: Session = Depends(get_db),
):
    service = DashboardService(db)
    return service.get_severity_distribution()


@router.get(
    "/threat-trend",
    response_model=list[ThreatTrendItem],
)
def get_threat_trend(
    db: Session = Depends(get_db),
):
    service = DashboardService(db)
    return service.get_threat_trend()
@router.get(
    "/events",
    response_model=list[AlertResponse],
)
def get_recent_events(
    db: Session = Depends(get_db),
):
    service = DashboardService(db)
    return service.get_recent_events()