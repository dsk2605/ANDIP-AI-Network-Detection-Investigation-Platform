from app.core.logging import get_logger
from app.detection.alert_category import AlertCategory
from app.detection.attack_types import AttackType
from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow
from app.detection.severity import Severity
from app.detection.thresholds import ICMP_FLOOD_THRESHOLD

logger = get_logger(__name__)


class IcmpFloodDetector(BaseDetector):
    """
    Detects ICMP Flood attacks.

    Counts ICMP packets from one source IP to one
    destination IP within a sliding time window.
    """

    WINDOW_SECONDS = 5
    COOLDOWN_SECONDS = 30

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        # ---------------------------------------
        # ICMP only
        # ---------------------------------------

        if flow.protocol.upper() != "ICMP":
            return None

        key = (
            flow.source_ip,
            flow.destination_ip,
        )

        # ---------------------------------------
        # Count NEW ICMP packets
        # ---------------------------------------

        self.state.add_counter(
            key,
            flow.packet_delta,
        )

        packet_count = self.state.get_counter(
            key,
            self.WINDOW_SECONDS,
        )

        logger.info(
            "[ICMP] %s -> %s | Count=%d | Threshold=%d",
            flow.source_ip,
            flow.destination_ip,
            packet_count,
            ICMP_FLOOD_THRESHOLD,
        )

        # ---------------------------------------
        # Threshold
        # ---------------------------------------

        if packet_count < ICMP_FLOOD_THRESHOLD:
            return None

        logger.info("[ICMP] Threshold reached.")

        # ---------------------------------------
        # Cooldown
        # ---------------------------------------

        if self.state.in_cooldown(
            key,
            self.COOLDOWN_SECONDS,
        ):
            logger.info("[ICMP] Cooldown active.")
            return None

        confidence = min(
            1.0,
            packet_count / (ICMP_FLOOD_THRESHOLD * 2),
        )

        logger.warning(
            "Potential ICMP Flood | %s -> %s | Packets=%d",
            flow.source_ip,
            flow.destination_ip,
            packet_count,
        )

        return DetectionResult(
            attack=AttackType.ICMP_FLOOD,
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
                f"Potential ICMP Flood detected "
                f"({packet_count} packets in "
                f"{self.WINDOW_SECONDS} seconds)."
            ),
            metadata={
                "packet_count": packet_count,
                "window_seconds": self.WINDOW_SECONDS,
                "threshold": ICMP_FLOOD_THRESHOLD,
            },
        )