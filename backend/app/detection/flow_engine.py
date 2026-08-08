from app.core.logging import get_logger
from app.detection.flow_manager import FlowManager

logger = get_logger(__name__)


class FlowEngine:

    def __init__(self):
        self.manager = FlowManager()

        logger.info("FlowEngine initialized.")

    def process(self, packet):

        logger.debug(
            "Processing packet into flow."
        )

        return self.manager.process_packet(packet)