import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import TimestampMixin


class DiscoveryStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ScanType(str, Enum):
    NMAP = "NMAP"
    MANUAL = "MANUAL"
    AGENT = "AGENT"


class DiscoveryScan(TimestampMixin, Base):
    __tablename__ = "discovery_scans"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    network: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    scan_type: Mapped[ScanType] = mapped_column(
        SQLEnum(ScanType),
        nullable=False,
        default=ScanType.NMAP,
    )

    status: Mapped[DiscoveryStatus] = mapped_column(
        SQLEnum(DiscoveryStatus),
        nullable=False,
        default=DiscoveryStatus.PENDING,
    )

    hosts_found: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )