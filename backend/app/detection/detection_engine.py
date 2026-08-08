from app.core.logging import get_logger
from app.detection.detector_registry import DetectorRegistry
from app.detection.attack_types import AttackType

logger = get_logger(__name__)


class DetectionEngine:
    """
    Central detection engine.

    Specialized detectors are given priority over the generic
    DoS detector to prevent duplicate classifications.

    Example:
        UDP Flood -> UDP Flood alert
        NOT UDP Flood + DoS

    Generic DoS is used as a fallback when traffic cannot be
    classified as a more specific denial-of-service attack.
    """

    # These attacks are more specific than generic DoS.
    # If one of these is detected for the same flow,
    # the generic DoS detector should not run.
    SPECIFIC_DOS_ATTACKS = {
        AttackType.DDOS,
        AttackType.SYN_FLOOD,
        AttackType.UDP_FLOOD,
        AttackType.ICMP_FLOOD,
        AttackType.HTTP_FLOOD,
    }

    def __init__(self):
        self.detectors = DetectorRegistry.get_detectors()

        logger.info(
            "Detection Engine initialized with %d detector(s).",
            len(self.detectors),
        )

    def analyze(self, flow):
        """
        Analyze a network flow using the registered detectors.

        Specialized attack detectors run first.

        Generic DoS is evaluated only when no specific
        DoS/flood classification was detected.
        """

        alerts = []

        if flow is None:
            return alerts

        # -------------------------------------------------
        # Separate generic DoS from specialized detectors
        # -------------------------------------------------

        specialized_detectors = []
        dos_detector = None

        for detector in self.detectors:

            if detector.__class__.__name__ == "DoSDetector":
                dos_detector = detector
            else:
                specialized_detectors.append(detector)

        # -------------------------------------------------
        # Run specialized detectors first
        # -------------------------------------------------

        for detector in specialized_detectors:

            try:

                logger.info(
                    "Running detector: %s",
                    detector.__class__.__name__,
                )

                result = detector.analyze(flow)

                if result:

                    logger.warning(
                        "%s DETECTED %s",
                        detector.__class__.__name__,
                        result.attack.value,
                    )

                    alerts.append(result)

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

        # -------------------------------------------------
        # Check whether a specific DoS attack was detected
        # -------------------------------------------------

        specific_dos_detected = any(
            alert.attack in self.SPECIFIC_DOS_ATTACKS
            for alert in alerts
        )

        # -------------------------------------------------
        # Run generic DoS only as a fallback
        # -------------------------------------------------

        if dos_detector is not None:

            if specific_dos_detected:

                logger.info(
                    "Specific DoS/flood attack detected. "
                    "Skipping generic DoS classification."
                )

            else:

                try:

                    logger.info(
                        "Running fallback detector: DoSDetector"
                    )

                    result = dos_detector.analyze(flow)

                    if result:

                        logger.warning(
                            "DoSDetector DETECTED %s",
                            result.attack.value,
                        )

                        alerts.append(result)

                    else:

                        logger.debug(
                            "DoSDetector returned None"
                        )

                except Exception:

                    logger.exception(
                        "Detector DoSDetector failed."
                    )

        # -------------------------------------------------
        # Final result
        # -------------------------------------------------

        if alerts:

            logger.info(
                "Detection Engine generated %d alert(s).",
                len(alerts),
            )

        return alerts