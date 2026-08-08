from app.alerts.manager import alert_manager
from app.collector.capture_engine import PacketCaptureEngine
from app.core.logging import get_logger
from app.detection.detection_engine import DetectionEngine
from app.detection.flow_engine import FlowEngine

logger = get_logger(__name__)


class PacketCaptureService:

    def __init__(self):
        self.engine = PacketCaptureEngine()
        self.flow_engine = FlowEngine()
        self.detection_engine = DetectionEngine()

    def start(self, interface=None):
        logger.info("=" * 60)
        logger.info("ANDIP Packet Collector Started")
        logger.info("=" * 60)

        self.engine.start_capture(
            interface=interface,
            packet_callback=self.process_packet,
        )

    def process_packet(self, packet):
        logger.debug("Packet received.")

        flow = self.flow_engine.process(packet)

        if flow:
            logger.info(
                "Flow created | %s:%s -> %s:%s | Protocol=%s | Packets=%d | Bytes=%d",
                flow.source_ip,
                flow.source_port,
                flow.destination_ip,
                flow.destination_port,
                flow.protocol,
                flow.packet_count,
                flow.total_bytes,
            )

        alerts = self.detection_engine.analyze(flow)

        if alerts:
            logger.warning(
                "Detection Engine generated %d alert(s).",
                len(alerts),
            )

        for alert in alerts:
            logger.warning(
                "Raising alert | Attack=%s | Severity=%s",
                alert.attack,
                alert.severity,
            )

            alert_manager.raise_alert(alert)

            logger.info("Alert stored successfully.")