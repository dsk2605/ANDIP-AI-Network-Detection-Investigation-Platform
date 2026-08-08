export interface DashboardOverview {
  total_alerts: number;
  critical: number;
  high: number;
  medium: number;
  low: number;
  today: number;
  top_attack: string | null;
  top_source_ip: string | null;
}

export interface SeverityDistributionItem {
  severity: string;
  count: number;
}

export interface ThreatTrendItem {
  time: string;
  alerts: number;
}

export interface RecentEvent {
  id: number;
  attack: string;
  severity: string;
  source_ip: string;
  destination_ip: string;
  timestamp: string;
}