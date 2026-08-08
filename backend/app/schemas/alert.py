from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class AlertResponse(BaseModel):
    id: int
    attack: str
    severity: str
    source_ip: str
    destination_ip: str | None
    description: str
    details: dict[str, Any]
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class PaginatedAlertsResponse(BaseModel):
    page: int
    limit: int
    total: int
    pages: int
    items: list[AlertResponse]