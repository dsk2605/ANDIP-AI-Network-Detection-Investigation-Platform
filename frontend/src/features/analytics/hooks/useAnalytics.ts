import { useQuery } from "@tanstack/react-query";


import {
  getAnalytics,
  getSeverityDistribution,
  getThreatTrend,
  getTopRiskAssets,
  getOSDistribution,
  getEnvironmentDistribution,
  getAssetTypeDistribution,
  getSecurityRecommendations,
  getDiscoverySummary,
} from "../services/analytics";

export function useAnalytics() {
  return useQuery({
    queryKey: ["analytics"],
    queryFn: getAnalytics,
    refetchInterval: 5000,
  });
}

export function useSeverityDistribution() {
  return useQuery({
    queryKey: [
      "analytics",
      "severity",
    ],
    queryFn: getSeverityDistribution,
    refetchInterval: 5000,
  });
}

export function useThreatTrend() {
  return useQuery({
    queryKey: [
      "analytics",
      "threat-trend",
    ],
    queryFn: getThreatTrend,
    refetchInterval: 5000,
  });
}

export function useTopRiskAssets() {
  return useQuery({
    queryKey: ["analytics", "top-risk-assets"],
    queryFn: getTopRiskAssets,
    refetchInterval: 10000,
  });
}

export function useOSDistribution() {
  return useQuery({
    queryKey: ["analytics", "os-distribution"],
    queryFn: getOSDistribution,
    refetchInterval: 30000,
  });
}

export function useEnvironmentDistribution() {
  return useQuery({
    queryKey: ["analytics", "environment-distribution"],
    queryFn: getEnvironmentDistribution,
    refetchInterval: 30000,
  });
}

export function useAssetTypeDistribution() {
  return useQuery({
    queryKey: ["analytics", "asset-type-distribution"],
    queryFn: getAssetTypeDistribution,
    refetchInterval: 30000,
  });
}

export function useSecurityRecommendations() {
  return useQuery({
    queryKey: ["analytics", "recommendations"],
    queryFn: getSecurityRecommendations,
    refetchInterval: 30000,
  });
}

export function useDiscoverySummary() {
  return useQuery({
    queryKey: ["analytics", "discovery-summary"],
    queryFn: getDiscoverySummary,
    refetchInterval: 30000,
  });
}