import uuid
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import TimestampMixin

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer

class AssetType(str, Enum):
    SERVER = "SERVER"
    WORKSTATION = "WORKSTATION"
    ROUTER = "ROUTER"
    FIREWALL = "FIREWALL"
    SWITCH = "SWITCH"
    VM = "VM"
    CONTAINER = "CONTAINER"
    OTHER = "OTHER"


class EnvironmentType(str, Enum):
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"
    TESTING = "TESTING"
    LAB = "LAB"


class AssetStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MAINTENANCE = "MAINTENANCE"


class Asset(TimestampMixin, Base):
    __tablename__ = "assets"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    hostname: Mapped[str] = mapped_column(String(255), nullable=False)

    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        unique=True,
    )

    mac_address: Mapped[str] = mapped_column(
        String(17),
        nullable=False,
        unique=True,
    )

    operating_system: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    asset_type: Mapped[AssetType] = mapped_column(
        SQLEnum(AssetType),
        nullable=False,
    )

    environment: Mapped[EnvironmentType] = mapped_column(
        SQLEnum(EnvironmentType),
        nullable=False,
    )

    status: Mapped[AssetStatus] = mapped_column(
        SQLEnum(AssetStatus),
        default=AssetStatus.ACTIVE,
        nullable=False,
    )

    last_seen: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    risk_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    is_monitored: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )