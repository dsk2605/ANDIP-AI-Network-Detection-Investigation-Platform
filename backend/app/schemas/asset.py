from pydantic import BaseModel, ConfigDict
from ipaddress import IPv4Address, IPv6Address
from typing import Union
from uuid import UUID
from datetime import datetime

from app.models.asset import (
    AssetStatus,
    AssetType,
    EnvironmentType,
)


class AssetCreate(BaseModel):
    hostname: str
    ip_address: Union[IPv4Address, IPv6Address]
    mac_address: str
    operating_system: str
    asset_type: AssetType
    environment: EnvironmentType


class AssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    hostname: str
    ip_address: str
    mac_address: str
    operating_system: str
    asset_type: AssetType
    environment: EnvironmentType
    status: AssetStatus

    last_seen: datetime | None
    risk_score: int
    is_monitored: bool

class AssetUpdate(BaseModel):
    hostname: str
    ip_address: Union[IPv4Address, IPv6Address]
    mac_address: str
    operating_system: str
    asset_type: AssetType
    environment: EnvironmentType
    status: AssetStatus        