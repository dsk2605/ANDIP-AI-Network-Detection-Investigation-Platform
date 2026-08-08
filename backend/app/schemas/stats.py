from pydantic import BaseModel


class AlertStatsResponse(BaseModel):
    total_alerts: int
    critical: int
    high: int
    medium: int
    low: int
    today: int
    top_attack: str | None
    top_source_ip: str | None