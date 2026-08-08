from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    attack: Mapped[str] = mapped_column(String(100), nullable=False)

    severity: Mapped[str] = mapped_column(String(30), nullable=False)

    source_ip: Mapped[str] = mapped_column(String(50), nullable=False)

    destination_ip: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    details: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )