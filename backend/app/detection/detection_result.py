from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from app.detection.attack_types import AttackType
from app.detection.alert_category import AlertCategory
from app.detection.severity import Severity


@dataclass(slots=True)
class DetectionResult:

    attack: AttackType

    category: AlertCategory

    severity: Severity

    source_ip: str

    destination_ip: str

    protocol: str

    confidence: float

    description: str

    metadata: dict[str, Any] = field(default_factory=dict)

    detected_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )