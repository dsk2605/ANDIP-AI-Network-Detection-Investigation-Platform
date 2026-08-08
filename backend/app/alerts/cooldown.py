from datetime import datetime, timedelta


class AlertCooldown:

    def __init__(self, cooldown_seconds: int = 60):
        self.cooldown = timedelta(seconds=cooldown_seconds)
        self.last_alerts: dict[str, datetime] = {}

    def can_alert(self, key: str) -> bool:
        now = datetime.utcnow()

        last_time = self.last_alerts.get(key)

        if last_time is None:
            self.last_alerts[key] = now
            return True

        if now - last_time >= self.cooldown:
            self.last_alerts[key] = now
            return True

        return False