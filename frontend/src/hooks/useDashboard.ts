import { useQuery } from "@tanstack/react-query";
import { getRecentEvents } from "@/services/dashboard";

import {
  getDashboardOverview,
  getSeverityDistribution,
  getThreatTrend,
} from "@/services/dashboard";

export function useDashboardOverview() {
  return useQuery({
    queryKey: ["dashboard-overview"],
    queryFn: getDashboardOverview,
    refetchInterval: 5000,
  });
}

export function useSeverityDistribution() {
  return useQuery({
    queryKey: ["severity-distribution"],
    queryFn: getSeverityDistribution,
    refetchInterval: 5000,
  });
}

export function useThreatTrend() {
  return useQuery({
    queryKey: ["threat-trend"],
    queryFn: getThreatTrend,
    refetchInterval: 5000,
  });
}

export function useRecentEvents() {
  return useQuery({
    queryKey: ["recent-events"],
    queryFn: getRecentEvents,
    refetchInterval: 5000,
  });
}