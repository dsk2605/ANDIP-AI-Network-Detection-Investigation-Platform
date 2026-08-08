import asyncio

from app.core.logging import get_logger
from app.events.event_bus import event_bus
from app.websocket.manager import manager

logger = get_logger(__name__)


class EventWorker:

    async def start(self):

        logger.info(
            "WebSocket Event Worker started."
        )

        while True:

            event = event_bus.get_event()

            if event:

                await manager.broadcast(event)

            await asyncio.sleep(0.05)


event_worker = EventWorker()