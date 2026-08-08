from app.core.logging import get_logger
from app.detection.alert_category import AlertCategory
from app.detection.attack_types import AttackType
from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow
from app.detection.severity import Severity
from app.detection.thresholds import DOS_THRESHOLD

logger = get_logger(__name__)


class DoSDetector(BaseDetector):
    """
    Detects generic Denial-of-Service attacks.

    Aggregates packets from one source IP
    to one destination IP across all flows.
    """

    WINDOW_SECONDS = 5
    COOLDOWN_SECONDS = 30

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        if not flow.protocol:
            return None

        key = (
            flow.source_ip,
            flow.destination_ip,
        )

        #
        # Add only NEW packets
        #
        self.state.add_counter(
            key,
            flow.packet_delta,
        )

        packet_count = self.state.get_counter(
            key,
            self.WINDOW_SECONDS,
        )

        logger.info(
            "[DoS] %s -> %s | Count=%d | Threshold=%d",
            flow.source_ip,
            flow.destination_ip,
            packet_count,
            DOS_THRESHOLD,
        )

        #
        # Threshold check
        #
        if packet_count < DOS_THRESHOLD:

            logger.debug(
                "[DoS] Waiting... (%d/%d)",
                packet_count,
                DOS_THRESHOLD,
            )

            return None

        logger.info(
            "[DoS] Threshold reached."
        )

        #
        # Detector cooldown
        #
        if self.state.in_cooldown(
            key,
            self.COOLDOWN_SECONDS,
        ):

            logger.info(
                "[DoS] Cooldown active."
            )

            return None

        logger.info(
            "[DoS] Generating alert."
        )

        confidence = min(
            1.0,
            packet_count / (DOS_THRESHOLD * 2),
        )

        logger.warning(
            "Potential DoS | Source=%s | Destination=%s | Packets=%d",
            flow.source_ip,
            flow.destination_ip,
            packet_count,
        )

        return DetectionResult(
            attack=AttackType.DOS,
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
                f"Potential DoS attack detected "
                f"({packet_count} packets in "
                f"{self.WINDOW_SECONDS} seconds)."
            ),
            metadata={
                "packet_count": packet_count,
                "window_seconds": self.WINDOW_SECONDS,
                "threshold": DOS_THRESHOLD,
            },
        )