import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import (
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import TimestampMixin


class DiscoverySource(str, Enum):
    NMAP = "NMAP"
    MANUAL = "MANUAL"
    SNMP = "SNMP"
    AGENT = "AGENT"


class ObservationStatus(str, Enum):
    NEW = "NEW"
    MATCHED = "MATCHED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class AssetObservation(TimestampMixin, Base):
    __tablename__ = "asset_observations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    scan_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("discovery_scans.id"),
        nullable=False,
    )

    asset_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assets.id"),
        nullable=True,
    )

    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
    )

    mac_address: Mapped[str | None] = mapped_column(
        String(17),
        nullable=True,
    )

    hostname: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    operating_system: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    vendor: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    source: Mapped[DiscoverySource] = mapped_column(
        SQLEnum(DiscoverySource),
        nullable=False,
    )

    status: Mapped[ObservationStatus] = mapped_column(
        SQLEnum(ObservationStatus),
        default=ObservationStatus.NEW,
        nullable=False,
    )

    confidence_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    ports: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    raw_scan_data: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    observed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )