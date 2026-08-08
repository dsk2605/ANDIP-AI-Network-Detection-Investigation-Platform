from app.core.logging import get_logger
from app.detection.alert_category import AlertCategory
from app.detection.attack_types import AttackType
from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow
from app.detection.severity import Severity
from app.detection.thresholds import UDP_FLOOD_THRESHOLD

logger = get_logger(__name__)


class UdpFloodDetector(BaseDetector):
    """
    Detects UDP Flood attacks using a sliding window.
    """

    WINDOW_SECONDS = 5
    COOLDOWN_SECONDS = 30

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        #
        # UDP only
        #
        if not flow.protocol:
            return None

        if flow.protocol.upper() != "UDP":
            return None

        #
        # Count UDP packets between source and destination
        #
        key = (
            flow.source_ip,
            flow.destination_ip,
        )

        self.state.add_event(
            key,
            1,
        )

        events = self.state.get_recent_events(
            key,
            self.WINDOW_SECONDS,
        )

        packet_count = len(events)

        if packet_count < UDP_FLOOD_THRESHOLD:
            return None

        if self.state.in_cooldown(
            key,
            self.COOLDOWN_SECONDS,
        ):
            return None

        confidence = min(
            1.0,
            packet_count / (UDP_FLOOD_THRESHOLD * 2),
        )

        logger.warning(
            "Potential UDP Flood | Source=%s | Destination=%s | Packets=%d",
            flow.source_ip,
            flow.destination_ip,
            packet_count,
        )

        return DetectionResult(
            attack=AttackType.UDP_FLOOD,
            category=AlertCategory.DENIAL_OF_SERVICE,
            severity=Severity.HIGH,
            source_ip=flow.source_ip,
            destination_ip=flow.destination_ip,
            protocol=flow.protocol,
            confidence=round(
                confidence,
                2,
            ),
            description=(
                f"Potential UDP Flood detected "
                f"({packet_count} UDP packets in "
                f"{self.WINDOW_SECONDS} seconds)."
            ),
            metadata={
                "packet_count": packet_count,
                "window_seconds": self.WINDOW_SECONDS,
                "threshold": UDP_FLOOD_THRESHOLD,
            },
        )