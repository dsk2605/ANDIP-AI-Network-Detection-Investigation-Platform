from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.database.repositories.alert_repository import AlertRepository
from app.schemas.alert import (
    AlertResponse,
    PaginatedAlertsResponse,
)
from app.schemas.stats import AlertStatsResponse
from app.services.alert_service import AlertService

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get(
    "",
    response_model=PaginatedAlertsResponse,
)
def get_alerts(
    page: int = Query(1, ge=1),
    limit: int = Query(25, ge=1, le=100),
    severity: str | None = None,
    attack: str | None = None,
    source_ip: str | None = None,
    destination_ip: str | None = None,
    search: str | None = None,
    start_date: datetime | None = Query(
        default=None,
        description="Filter alerts from date (YYYY-MM-DD)",
    ),
    end_date: datetime | None = Query(
        default=None,
        description="Filter alerts until date (YYYY-MM-DD)",
    ),
    sort: str = Query(
        default="desc",
        pattern="^(asc|desc)$",
    ),
    db: Session = Depends(get_db),
):
    service = AlertService(AlertRepository(db))

    return service.get_alerts(
        page=page,
        limit=limit,
        severity=severity,
        attack=attack,
        source_ip=source_ip,
        destination_ip=destination_ip,
        search=search,
        start_date=start_date,
        end_date=end_date,
        sort=sort,
    )


@router.get(
    "/stats",
    response_model=AlertStatsResponse,
)
def get_alert_stats(
    db: Session = Depends(get_db),
):
    service = AlertService(AlertRepository(db))
    return service.get_stats()


@router.get(
    "/{alert_id}",
    response_model=AlertResponse,
)
def get_alert(
    alert_id: int,
    db: Session = Depends(get_db),
):
    service = AlertService(AlertRepository(db))

    alert = service.get_alert_by_id(alert_id)

    if alert is None:
        raise HTTPException(
            status_code=404,
            detail="Alert not found",
        )

    return alert