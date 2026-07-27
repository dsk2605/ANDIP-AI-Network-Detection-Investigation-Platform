from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate, AssetResponse
from app.services.risk_engine import calculate_risk


router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)


@router.post("/", response_model=AssetResponse)
def create_asset(
    asset: AssetCreate,
    db: Session = Depends(get_db),
):
    risk_score = calculate_risk(
        operating_system=asset.operating_system,
        asset_type=asset.asset_type,
        environment=asset.environment,
        is_monitored=True,
    )

    db_asset = Asset(
        hostname=asset.hostname,
        ip_address=str(asset.ip_address),
        mac_address=asset.mac_address,
        operating_system=asset.operating_system,
        asset_type=asset.asset_type,
        environment=asset.environment,
        risk_score=risk_score,
    )

    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)

    return db_asset


@router.get("/", response_model=List[AssetResponse])
def get_assets(db: Session = Depends(get_db)):
    return db.query(Asset).all()


@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return asset


@router.put("/{asset_id}", response_model=AssetResponse)
def update_asset(
    asset_id: UUID,
    updated_asset: AssetUpdate,
    db: Session = Depends(get_db),
):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    asset.hostname = updated_asset.hostname
    asset.ip_address = str(updated_asset.ip_address)
    asset.mac_address = updated_asset.mac_address
    asset.operating_system = updated_asset.operating_system
    asset.asset_type = updated_asset.asset_type
    asset.environment = updated_asset.environment
    asset.status = updated_asset.status

    asset.risk_score = calculate_risk(
        operating_system=asset.operating_system,
        asset_type=asset.asset_type,
        environment=asset.environment,
        is_monitored=asset.is_monitored,
    )

    db.commit()
    db.refresh(asset)

    return asset


@router.delete("/{asset_id}")
def delete_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    db.delete(asset)
    db.commit()

    return JSONResponse(
        status_code=200,
        content={
            "message": "Asset deleted successfully"
        },
    )