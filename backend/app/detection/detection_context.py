from collections import defaultdict, deque
from datetime import datetime, timedelta


class DetectionContext:

    def __init__(self):

        self.windows = defaultdict(deque)

    def add_event(
        self,
        key,
        value,
    ):

        self.windows[key].append(
            (
                datetime.utcnow(),
                value,
            )
        )

    def get_window(
        self,
        key,
        seconds,
    ):

        queue = self.windows[key]

        cutoff = datetime.utcnow() - timedelta(
            seconds=seconds
        )

        while queue and queue[0][0] < cutoff:
            queue.popleft()

        return list(queue)

    def clear(
        self,
        key,
    ):
        self.windows.pop(key, None)