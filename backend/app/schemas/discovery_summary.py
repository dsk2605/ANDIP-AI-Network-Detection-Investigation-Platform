from datetime import datetime

from pydantic import BaseModel


class DiscoverySummaryResponse(BaseModel):

    total_scans: int

    total_hosts_discovered: int

    average_hosts_per_scan: float

    latest_scan: datetime | None