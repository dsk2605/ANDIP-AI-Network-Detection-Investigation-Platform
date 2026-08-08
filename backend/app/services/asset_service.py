from uuid import UUID

from app.database.repositories.asset_repository import AssetRepository
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate
from app.services.risk_engine import calculate_risk


class AssetService:

    def __init__(self, repository: AssetRepository):
        self.repository = repository

    def create_asset(self, asset_data: AssetCreate):

        risk_score = calculate_risk(
            operating_system=asset_data.operating_system,
            asset_type=asset_data.asset_type,
            environment=asset_data.environment,
            is_monitored=True,
        )

        asset = Asset(
            hostname=asset_data.hostname,
            ip_address=str(asset_data.ip_address),
            mac_address=asset_data.mac_address,
            operating_system=asset_data.operating_system,
            asset_type=asset_data.asset_type,
            environment=asset_data.environment,
            risk_score=risk_score,
        )

        return self.repository.create(asset)

    def get_assets(self):
        return self.repository.get_all()

    def get_asset(self, asset_id: UUID):
        return self.repository.get_by_id(asset_id)

    def update_asset(
        self,
        asset: Asset,
        updated: AssetUpdate,
    ):

        asset.hostname = updated.hostname
        asset.ip_address = str(updated.ip_address)
        asset.mac_address = updated.mac_address
        asset.operating_system = updated.operating_system
        asset.asset_type = updated.asset_type
        asset.environment = updated.environment
        asset.status = updated.status

        asset.risk_score = calculate_risk(
            operating_system=asset.operating_system,
            asset_type=asset.asset_type,
            environment=asset.environment,
            is_monitored=asset.is_monitored,
        )

        return self.repository.update(asset)

    def delete_asset(self, asset: Asset):
        self.repository.delete(asset)