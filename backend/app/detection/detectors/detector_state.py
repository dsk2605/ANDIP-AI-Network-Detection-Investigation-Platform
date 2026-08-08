from collections import defaultdict, deque
from datetime import datetime, timedelta

from app.core.logging import get_logger

logger = get_logger(__name__)


class DetectorState:
    """
    Shared state manager for all detectors.

    Supports:
    - Sliding-window events
    - Sliding-window counters
    - Unique value tracking
    - Cooldowns
    """

    def __init__(self):

        # Sliding window events
        self.events = defaultdict(deque)

        # Sliding window counters
        self.counters = defaultdict(deque)

        # Sliding window unique values
        self.unique_values = defaultdict(deque)

        # Detector cooldowns
        self.cooldowns = {}

    # =====================================================
    # Events
    # =====================================================

    def add_event(
        self,
        key,
        value,
    ):

        self.events[key].append(
            (
                datetime.now(),
                value,
            )
        )

    def get_recent_events(
        self,
        key,
        window_seconds,
    ):

        now = datetime.now()

        window = timedelta(
            seconds=window_seconds,
        )

        q = self.events[key]

        while q and (
            now - q[0][0]
        ) > window:
            q.popleft()

        return list(q)

    # =====================================================
    # Counters
    # =====================================================

    def add_counter(
        self,
        key,
        value,
    ):

        self.counters[key].append(
            (
                datetime.now(),
                value,
            )
        )

    def get_counter(
        self,
        key,
        window_seconds,
    ):

        now = datetime.now()

        window = timedelta(
            seconds=window_seconds,
        )

        q = self.counters[key]

        while q and (
            now - q[0][0]
        ) > window:
            q.popleft()

        return sum(
            value
            for _, value in q
        )

    # =====================================================
    # Unique Values
    # =====================================================

    def add_unique(
        self,
        key,
        value,
    ):

        self.unique_values[key].append(
            (
                datetime.now(),
                value,
            )
        )

    def get_unique(
        self,
        key,
        window_seconds,
    ):

        now = datetime.now()

        window = timedelta(
            seconds=window_seconds,
        )

        q = self.unique_values[key]

        while q and (
            now - q[0][0]
        ) > window:
            q.popleft()

        return {
            value
            for _, value in q
        }

    # =====================================================
    # Cooldown
    # =====================================================

    def in_cooldown(
        self,
        key,
        cooldown_seconds,
    ):

        now = datetime.now()

        last = self.cooldowns.get(key)

        # ---------------------------------------
        # First detection
        # ---------------------------------------

        if last is None:

            logger.info(
                "[Cooldown] FIRST ALERT | Key=%s",
                key,
            )

            self.cooldowns[key] = now

            return False

        elapsed = (
            now - last
        ).total_seconds()

        # ---------------------------------------
        # Cooldown active
        # ---------------------------------------

        if elapsed < cooldown_seconds:

            logger.info(
                "[Cooldown] ACTIVE | Key=%s | %.2fs remaining",
                key,
                cooldown_seconds - elapsed,
            )

            return True

        # ---------------------------------------
        # Cooldown expired
        # ---------------------------------------

        logger.info(
            "[Cooldown] EXPIRED | Key=%s",
            key,
        )

        self.cooldowns[key] = now

        return False