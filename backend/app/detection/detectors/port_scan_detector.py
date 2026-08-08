from app.core.logging import get_logger
from app.detection.alert_category import AlertCategory
from app.detection.attack_types import AttackType
from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow
from app.detection.severity import Severity
from app.detection.thresholds import (
    PORT_SCAN_THRESHOLD,
)

logger = get_logger(__name__)


class PortScanDetector(BaseDetector):
    """
    Detects TCP Port Scans using a sliding window.
    """

    WINDOW_SECONDS = 5
    COOLDOWN_SECONDS = 30

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        if flow.protocol.upper() != "TCP":
            return None

        if flow.destination_port is None:
            return None

        key = flow.source_ip

        self.state.add_event(
            key,
            flow.destination_port,
        )

        events = self.state.get_recent_events(
            key,
            self.WINDOW_SECONDS,
        )

        ports = {
            port
            for _, port in events
        }

        if len(ports) < PORT_SCAN_THRESHOLD:
            return None

        if self.state.in_cooldown(
            key,
            self.COOLDOWN_SECONDS,
        ):
            return None

        confidence = min(
            1.0,
            len(ports) / 50,
        )

        logger.warning(
            "Potential Port Scan | Source=%s | Ports=%d",
            flow.source_ip,
            len(ports),
        )

        return DetectionResult(
            attack=AttackType.PORT_SCAN,
            category=AlertCategory.RECONNAISSANCE,
            severity=Severity.MEDIUM,
            source_ip=flow.source_ip,
            destination_ip=flow.destination_ip,
            protocol=flow.protocol,
            confidence=round(
                confidence,
                2,
            ),
            description=(
                f"Detected scan of "
                f"{len(ports)} unique ports "
                f"in the last "
                f"{self.WINDOW_SECONDS} seconds."
            ),
            metadata={
                "ports_scanned": len(ports),
                "ports": sorted(ports),
                "window_seconds": self.WINDOW_SECONDS,
            },
        )