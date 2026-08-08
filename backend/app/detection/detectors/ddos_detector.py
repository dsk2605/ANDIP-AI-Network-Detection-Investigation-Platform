from app.core.logging import get_logger
from app.detection.alert_category import AlertCategory
from app.detection.attack_types import AttackType
from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow
from app.detection.severity import Severity
from app.detection.thresholds import (
    DDOS_PACKET_THRESHOLD,
    DDOS_SOURCE_THRESHOLD,
)

logger = get_logger(__name__)


class DDoSDetector(BaseDetector):
    """
    Detects Distributed Denial-of-Service attacks.

    Detection requires:

    - High packet volume
    - Multiple unique attacking sources
    - Same destination
    - Sliding time window
    """

    WINDOW_SECONDS = 5
    COOLDOWN_SECONDS = 30

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        if not flow.destination_ip:
            return None

        key = flow.destination_ip

        #
        # Track packet volume
        #
        self.state.add_counter(
            key,
            flow.packet_delta,
        )

        #
        # Track unique attacking IPs
        #
        self.state.add_unique(
            key,
            flow.source_ip,
        )

        packet_count = self.state.get_counter(
            key,
            self.WINDOW_SECONDS,
        )

        unique_sources = len(
            self.state.get_unique(
                key,
                self.WINDOW_SECONDS,
            )
        )

        logger.info(
            "[DDoS] Target=%s | Packets=%d | Sources=%d",
            flow.destination_ip,
            packet_count,
            unique_sources,
        )

        #
        # Packet threshold
        #
        if packet_count < DDOS_PACKET_THRESHOLD:
            return None

        #
        # Source threshold
        #
        if unique_sources < DDOS_SOURCE_THRESHOLD:
            return None

        logger.info("[DDoS] Threshold reached.")

        #
        # Cooldown
        #
        if self.state.in_cooldown(
            key,
            self.COOLDOWN_SECONDS,
        ):
            logger.info("[DDoS] Cooldown active.")
            return None

        confidence = min(
            1.0,
            (
                (packet_count / DDOS_PACKET_THRESHOLD)
                +
                (unique_sources / DDOS_SOURCE_THRESHOLD)
            ) / 2,
        )

        logger.warning(
            "Potential DDoS | Target=%s | Sources=%d | Packets=%d",
            flow.destination_ip,
            unique_sources,
            packet_count,
        )

        return DetectionResult(
            attack=AttackType.DDOS,
            category=AlertCategory.DENIAL_OF_SERVICE,
            severity=Severity.CRITICAL,
            source_ip=flow.source_ip,
            destination_ip=flow.destination_ip,
            protocol=flow.protocol,
            confidence=round(
                confidence,
                2,
            ),
            description=(
                f"Potential DDoS attack detected "
                f"({unique_sources} attacking sources, "
                f"{packet_count} packets in "
                f"{self.WINDOW_SECONDS} seconds)."
            ),
            metadata={
                "unique_sources": unique_sources,
                "packet_count": packet_count,
                "window_seconds": self.WINDOW_SECONDS,
                "packet_threshold": DDOS_PACKET_THRESHOLD,
                "source_threshold": DDOS_SOURCE_THRESHOLD,
            },
        )