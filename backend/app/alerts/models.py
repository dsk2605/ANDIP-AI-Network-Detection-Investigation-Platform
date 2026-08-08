from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Alert:

    attack: str
    severity: str
    source_ip: str

    destination_ip: str | None = None

    description: str = ""

    details: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(default_factory=datetime.utcnow)