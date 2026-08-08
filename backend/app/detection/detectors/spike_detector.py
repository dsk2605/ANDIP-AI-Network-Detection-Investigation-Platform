from app.core.logging import get_logger
from app.detection.alert_category import AlertCategory
from app.detection.attack_types import AttackType
from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow
from app.detection.severity import Severity
from app.detection.thresholds import (
    TRAFFIC_SPIKE_MIN_PACKETS,
    TRAFFIC_SPIKE_PPS_THRESHOLD,
)

logger = get_logger(__name__)


class SpikeDetector(BaseDetector):
    """
    Detects abnormal traffic spikes.

    A spike is characterized by unusually high
    packet and bandwidth rates over a flow.
    """

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        #
        # Ignore tiny flows
        #
        if flow.packet_count < TRAFFIC_SPIKE_MIN_PACKETS:
            return None

        pps = flow.packets_per_second
        bps = flow.bytes_per_second

        if pps < TRAFFIC_SPIKE_PPS_THRESHOLD:
            return None

        confidence = min(
            1.0,
            pps / (TRAFFIC_SPIKE_PPS_THRESHOLD * 2),
        )

        logger.warning(
            "Traffic Spike | %s -> %s | PPS=%.2f | BPS=%.2f",
            flow.source_ip,
            flow.destination_ip,
            pps,
            bps,
        )

        return DetectionResult(

            attack=AttackType.TRAFFIC_SPIKE,

            category=AlertCategory.ANOMALY,

            severity=Severity.MEDIUM,

            source_ip=flow.source_ip,

            destination_ip=flow.destination_ip,

            protocol=flow.protocol,

            confidence=round(
                confidence,
                2,
            ),

            description=(
                f"Traffic spike detected "
                f"({pps:.2f} packets/sec)."
            ),

            metadata={
                "packets_per_second": round(pps, 2),
                "bytes_per_second": round(bps, 2),
                "packet_count": flow.packet_count,
                "total_bytes": flow.total_bytes,
                "duration": round(flow.duration_seconds, 2),
            },
        )