export interface Alert {
  id: number;

  attack: string;

  severity: string;

  source_ip: string;

  destination_ip: string;

  description: string;

  timestamp: string;

  details: Record<string, unknown>;
}

export interface AlertsResponse {
  page: number;
  limit: number;
  total: number;
  pages: number;
  items: Alert[];
}