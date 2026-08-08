from uuid import UUID

from sqlalchemy.orm import Session

from app.models.asset import Asset


class AssetRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, asset: Asset):
        try:
            self.db.add(asset)
            self.db.commit()
            self.db.refresh(asset)
            return asset

        except Exception:
            self.db.rollback()
            raise

    def get_all(self):
        return self.db.query(Asset).all()

    def get_by_id(self, asset_id: UUID):
        return (
            self.db.query(Asset)
            .filter(Asset.id == asset_id)
            .first()
        )

    def update(self, asset: Asset):
        try:
            self.db.commit()
            self.db.refresh(asset)
            return asset

        except Exception:
            self.db.rollback()
            raise

    def delete(self, asset: Asset):
        try:
            self.db.delete(asset)
            self.db.commit()

        except Exception:
            self.db.rollback()
            raise

    def count(self):
        return self.db.query(Asset).count()