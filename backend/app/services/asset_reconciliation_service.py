from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.asset import (
    Asset,
    AssetStatus,
    AssetType,
    EnvironmentType,
)
from app.models.asset_observation import AssetObservation


class AssetReconciliationService:

    def __init__(self, db: Session):
        self.db = db

    def reconcile(
        self,
        observation: AssetObservation,
    ) -> Asset:

        asset = (
            self.db.query(Asset)
            .filter(
                Asset.ip_address == observation.ip_address
            )
            .first()
        )

        if asset:

            asset.last_seen = datetime.now(timezone.utc)

            if observation.hostname:
                asset.hostname = observation.hostname

            if observation.operating_system:
                asset.operating_system = observation.operating_system

            if observation.mac_address:
                asset.mac_address = observation.mac_address

        else:

            asset = Asset(

                hostname=observation.hostname
                or observation.ip_address,

                ip_address=observation.ip_address,

                mac_address=observation.mac_address
                or "00:00:00:00:00:00",

                operating_system=observation.operating_system
                or "Unknown",

                asset_type=AssetType.OTHER,

                environment=EnvironmentType.LAB,

                status=AssetStatus.ACTIVE,

                last_seen=datetime.now(timezone.utc),

                risk_score=0,

                is_monitored=True,
            )

            self.db.add(asset)

            self.db.flush()

        observation.asset_id = asset.id

        return asset