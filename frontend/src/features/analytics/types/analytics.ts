export interface AnalyticsSummary {
  totalAlerts: number;
  criticalAlerts: number;
  totalAssets: number;
  totalScans: number;
  averageRiskScore: number;
}

export interface SeverityDistribution {
  severity: string;
  count: number;
}

export interface ThreatTrend {
  time: string;
  alerts: number;
}

export interface TopRiskAsset {
  id: string;
  hostname: string;
  ip_address: string;
  operating_system: string;
  asset_type: string;
  environment: string;
  status: string;
  risk_score: number;
}

export interface OSDistribution {
  operating_system: string;
  count: number;
}

export interface EnvironmentDistribution {
  environment: string;
  count: number;
}

export interface AssetTypeDistribution {
  asset_type: string;
  count: number;
}

export interface SecurityRecommendation {
  priority: string;
  message: string;
}

export interface DiscoverySummary {
  total_scans: number;
  total_hosts_discovered: number;
  average_hosts_per_scan: number;
  latest_scan: string | null;
}