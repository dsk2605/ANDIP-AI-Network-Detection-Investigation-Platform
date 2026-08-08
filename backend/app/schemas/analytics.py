from pydantic import BaseModel


class AnalyticsResponse(BaseModel):

    total_alerts: int

    critical_alerts: int

    total_assets: int

    total_scans: int

    average_risk_score: float