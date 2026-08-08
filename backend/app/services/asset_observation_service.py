from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.asset_observation import (
    AssetObservation,
    DiscoverySource,
    ObservationStatus,
)


class AssetObservationService:
    """Handles Asset Observation persistence."""

    def __init__(self, db: Session):
        self.db = db

    def create_observation(
        self,
        scan_id,
        asset_data: dict,
    ) -> AssetObservation:

        observation = AssetObservation(
            scan_id=scan_id,
            ip_address=asset_data["ip_address"],
            mac_address=asset_data.get("mac_address"),
            hostname=asset_data.get("hostname"),
            operating_system=asset_data.get("operating_system"),
            vendor=asset_data.get("vendor"),
            ports=asset_data.get("ports"),
            raw_scan_data=asset_data,
            source=DiscoverySource.NMAP,
            status=ObservationStatus.NEW,
            confidence_score=100,
            observed_at=datetime.now(timezone.utc),
        )

        self.db.add(observation)
        self.db.flush()

        return observation