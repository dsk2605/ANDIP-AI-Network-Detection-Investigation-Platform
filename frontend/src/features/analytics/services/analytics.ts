import api from "@/services/api";

import type {
  AnalyticsSummary,
  SeverityDistribution,
  ThreatTrend,
  OSDistribution,
  EnvironmentDistribution,
  AssetTypeDistribution,
  SecurityRecommendation,
  DiscoverySummary,
} from "../types/analytics";

export async function getAnalytics(): Promise<AnalyticsSummary> {
  const response = await api.get("/analytics/overview");

  return {
    totalAlerts: response.data.total_alerts,
    criticalAlerts: response.data.critical_alerts,
    totalAssets: response.data.total_assets,
    totalScans: response.data.total_scans,
    averageRiskScore: response.data.average_risk_score,
  };
}

export async function getSeverityDistribution(): Promise<
  SeverityDistribution[]
> {
  const response = await api.get(
    "/dashboard/severity-distribution",
  );

  return response.data;
}

export async function getThreatTrend(): Promise<
  ThreatTrend[]
> {
  const response = await api.get(
    "/dashboard/threat-trend"
  );

  return response.data;
}

import type { TopRiskAsset } from "../types/analytics";

export async function getTopRiskAssets(): Promise<
  TopRiskAsset[]
> {
  const response = await api.get(
    "/analytics/top-risk-assets"
  );

  return response.data;
}

export async function getOSDistribution(): Promise<
  OSDistribution[]
> {
  const response = await api.get(
    "/analytics/os-distribution"
  );

  return response.data;
}

export async function getEnvironmentDistribution(): Promise<
  EnvironmentDistribution[]
> {
  const response = await api.get(
    "/analytics/environment-distribution"
  );

  return response.data;
}

export async function getAssetTypeDistribution(): Promise<
  AssetTypeDistribution[]
> {
  const response = await api.get(
    "/analytics/asset-type-distribution"
  );

  return response.data;
}

export async function getSecurityRecommendations(): Promise<
  SecurityRecommendation[]
> {
  const response = await api.get(
    "/analytics/security-recommendations"
  );

  return response.data;
}

export async function getDiscoverySummary(): Promise<
  DiscoverySummary
> {
  const response = await api.get(
    "/analytics/discovery-summary"
  );

  return response.data;
}