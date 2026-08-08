from app.core.logging import get_logger
from app.detection.alert_category import AlertCategory
from app.detection.attack_types import AttackType
from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow
from app.detection.severity import Severity
from app.detection.thresholds import SYN_FLOOD_THRESHOLD

logger = get_logger(__name__)


class SynFloodDetector(BaseDetector):
    """
    Detects TCP SYN Flood attacks.

    Detects repeated SYN packets from one source IP
    to one destination IP and one destination port
    within a sliding time window.
    """

    WINDOW_SECONDS = 5
    COOLDOWN_SECONDS = 30

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        # ---------------------------------------
        # TCP only
        # ---------------------------------------

        if flow.protocol.upper() != "TCP":
            return None

        # ---------------------------------------
        # Count only pure SYN packets
        # ---------------------------------------

        if flow.tcp_flags != "S":
            return None

        # ---------------------------------------
        # Group by service (destination port)
        # ---------------------------------------

        key = (
            flow.source_ip,
            flow.destination_ip,
            flow.destination_port,
        )

        self.state.add_counter(
            key,
            flow.packet_delta,
        )

        syn_count = self.state.get_counter(
            key,
            self.WINDOW_SECONDS,
        )

        # ---------------------------------------
        # Threshold
        # ---------------------------------------

        if syn_count < SYN_FLOOD_THRESHOLD:
            return None

        # ---------------------------------------
        # Cooldown
        # ---------------------------------------

        if self.state.in_cooldown(
            key,
            self.COOLDOWN_SECONDS,
        ):
            return None

        confidence = min(
            1.0,
            syn_count / (SYN_FLOOD_THRESHOLD * 2),
        )

        logger.warning(
            "Potential SYN Flood | %s -> %s:%s | SYN=%d",
            flow.source_ip,
            flow.destination_ip,
            flow.destination_port,
            syn_count,
        )

        return DetectionResult(
            attack=AttackType.SYN_FLOOD,
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
                f"Potential SYN Flood detected against "
                f"port {flow.destination_port} "
                f"({syn_count} SYN packets in "
                f"{self.WINDOW_SECONDS} seconds)."
            ),
            metadata={
                "destination_port": flow.destination_port,
                "syn_packets": syn_count,
                "window_seconds": self.WINDOW_SECONDS,
                "threshold": SYN_FLOOD_THRESHOLD,
                "tcp_flags": flow.tcp_flags,
            },
        )