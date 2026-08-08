import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.discovery.discovery_service import DiscoveryService
from app.models.discovery_scan import (
    DiscoveryScan,
    DiscoveryStatus,
    ScanType,
)
from app.schemas.discovery import (
    DiscoveryScanRequest,
    DiscoveryScanResponse,
    DiscoveryScanHistory,
)

router = APIRouter(
    prefix="/discovery",
    tags=["Discovery"],
)


@router.post("/scan", response_model=DiscoveryScanResponse)
def run_discovery_scan(
    request: DiscoveryScanRequest,
    db: Session = Depends(get_db),
):

    scan = DiscoveryScan(
        network=request.target,
        scan_type=ScanType.NMAP,
        status=DiscoveryStatus.RUNNING,
        started_at=datetime.datetime.utcnow(),
    )

    db.add(scan)
    db.commit()
    db.refresh(scan)

    service = DiscoveryService(db)

    observations = service.discover(
        target=request.target,
        scan_id=scan.id,
    )

    scan.status = DiscoveryStatus.COMPLETED
    scan.finished_at = datetime.datetime.utcnow()
    scan.hosts_found = len(observations)

    db.commit()

    return DiscoveryScanResponse(
        message="Discovery completed successfully.",
        scan_id=str(scan.id),
        assets_discovered=len(observations),
    )


@router.get(
    "/scans",
    response_model=list[DiscoveryScanHistory],
)
def get_discovery_scans(
    db: Session = Depends(get_db),
):

    scans = (
        db.query(DiscoveryScan)
        .order_by(DiscoveryScan.started_at.desc())
        .all()
    )

    return [
        DiscoveryScanHistory(
            id=str(scan.id),
            network=scan.network,
            scan_type=scan.scan_type.value,
            status=scan.status.value,
            hosts_found=scan.hosts_found,
            started_at=scan.started_at.isoformat()
            if scan.started_at
            else None,
            finished_at=scan.finished_at.isoformat()
            if scan.finished_at
            else None,
        )
        for scan in scans
    ]