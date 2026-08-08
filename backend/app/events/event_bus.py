from queue import Queue
from typing import Any


class EventBus:

    def __init__(self):
        self._queue: Queue[dict[str, Any]] = Queue()

    def publish(
        self,
        event: dict[str, Any],
    ) -> None:

        self._queue.put(event)

    def has_events(self) -> bool:

        return not self._queue.empty()

    def get_event(self) -> dict[str, Any] | None:

        if self._queue.empty():
            return None

        return self._queue.get()


event_bus = EventBus()