from pydantic import BaseModel


class DashboardOverviewResponse(BaseModel):
    total_alerts: int
    critical: int
    high: int
    medium: int
    low: int
    today: int

    top_attack: str | None
    top_source_ip: str | None


class SeverityDistributionItem(BaseModel):
    severity: str
    count: int


class ThreatTrendItem(BaseModel):
    time: str
    alerts: int