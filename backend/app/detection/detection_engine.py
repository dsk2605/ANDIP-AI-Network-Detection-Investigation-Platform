from app.core.logging import get_logger
from app.detection.attack_types import AttackType
from app.detection.detector_registry import DetectorRegistry

logger = get_logger(__name__)


class DetectionEngine:

    def __init__(self):

        self.detectors = DetectorRegistry.get_detectors()

        logger.info(
            "Detection Engine initialized with %d detector(s).",
            len(self.detectors),
        )

        #
        # Higher number = Higher priority
        #
        self.attack_priority = {
            AttackType.DDOS: 100,
            AttackType.UDP_FLOOD: 90,
            AttackType.SYN_FLOOD: 90,
            AttackType.ICMP_FLOOD: 90,
            AttackType.PORT_SCAN: 80,
            AttackType.DOS: 10,
        }

    def analyze(self, flow):

        if flow is None:
            return []

        detected_alerts = []

        for detector in self.detectors:

            try:

                logger.info(
                    "Running detector: %s",
                    detector.__class__.__name__,
                )

                result = detector.analyze(flow)

                if result:

                    logger.warning(
                        "%s detected %s",
                        detector.__class__.__name__,
                        result.attack.value,
                    )

                    detected_alerts.append(result)

                else:

                    logger.debug(
                        "%s returned None",
                        detector.__class__.__name__,
                    )

            except Exception:

                logger.exception(
                    "Detector %s failed.",
                    detector.__class__.__name__,
                )

        #
        # Nothing detected
        #
        if not detected_alerts:
            return []

        #
        # Choose highest-priority alert
        #
        highest = max(
            detected_alerts,
            key=lambda alert: self.attack_priority.get(
                alert.attack,
                0,
            ),
        )

        logger.info(
            "Selected alert: %s",
            highest.attack.value,
        )

        return [highest]