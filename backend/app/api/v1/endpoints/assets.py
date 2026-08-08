from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.database.repositories.asset_repository import AssetRepository
from app.schemas.asset import (
    AssetCreate,
    AssetResponse,
    AssetUpdate,
)
from app.services.asset_service import AssetService

router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)


@router.post(
    "/",
    response_model=AssetResponse,
)
def create_asset(
    asset: AssetCreate,
    db: Session = Depends(get_db),
):
    service = AssetService(
        AssetRepository(db)
    )

    return service.create_asset(asset)


@router.get(
    "/",
    response_model=List[AssetResponse],
)
def get_assets(
    db: Session = Depends(get_db),
):
    service = AssetService(
        AssetRepository(db)
    )

    return service.get_assets()


@router.get(
    "/{asset_id}",
    response_model=AssetResponse,
)
def get_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
):
    service = AssetService(
        AssetRepository(db)
    )

    asset = service.get_asset(asset_id)

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return asset


@router.put(
    "/{asset_id}",
    response_model=AssetResponse,
)
def update_asset(
    asset_id: UUID,
    updated_asset: AssetUpdate,
    db: Session = Depends(get_db),
):
    service = AssetService(
        AssetRepository(db)
    )

    asset = service.get_asset(asset_id)

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return service.update_asset(
        asset,
        updated_asset,
    )


@router.delete(
    "/{asset_id}",
)
def delete_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
):
    service = AssetService(
        AssetRepository(db)
    )

    asset = service.get_asset(asset_id)

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    service.delete_asset(asset)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Asset deleted successfully",
        },
    )