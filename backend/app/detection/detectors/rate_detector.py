from abc import ABC

from app.detection.detectors.base_detector import BaseDetector
from app.detection.detection_result import DetectionResult
from app.detection.flow import NetworkFlow


class RateDetector(BaseDetector, ABC):

    THRESHOLD = 0
    ATTACK = None
    CATEGORY = None
    SEVERITY = None
    PROTOCOL = None

    def analyze(
        self,
        flow: NetworkFlow,
    ) -> DetectionResult | None:

        if self.PROTOCOL:

            if flow.protocol.upper() != self.PROTOCOL:
                return None

        key = (
            flow.source_ip,
            flow.destination_ip,
        )

        self.context.add_event(
            key,
            flow.packet_count,
        )

        events = self.context.get_window(
            key,
            self.WINDOW_SECONDS,
        )

        packets = len(events)

        pps = packets / self.WINDOW_SECONDS

        if pps < self.THRESHOLD:
            return None

        if self.state.in_cooldown(
            key,
            self.COOLDOWN_SECONDS,
        ):
            return None

        confidence = min(
            1.0,
            pps / self.THRESHOLD,
        )

        return DetectionResult(

            attack=self.ATTACK,

            category=self.CATEGORY,

            severity=self.SEVERITY,

            source_ip=flow.source_ip,

            destination_ip=flow.destination_ip,

            protocol=flow.protocol,

            confidence=round(
                confidence,
                2,
            ),

            description=(
                f"{self.ATTACK.value} detected "
                f"({pps:.2f} packets/sec)."
            ),

            metadata={

                "pps": round(
                    pps,
                    2,
                ),

                "window": self.WINDOW_SECONDS,

            },
        )