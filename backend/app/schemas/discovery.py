from pydantic import BaseModel


class DiscoveryScanRequest(BaseModel):
    target: str


class DiscoveryScanResponse(BaseModel):
    message: str
    scan_id: str
    assets_discovered: int


class DiscoveryScanHistory(BaseModel):
    id: str
    network: str
    scan_type: str
    status: str
    hosts_found: int
    started_at: str | None
    finished_at: str | None