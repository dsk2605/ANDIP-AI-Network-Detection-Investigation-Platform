import api from "./api";
import type { RecentEvent } from "@/types/dashboard";

import type {
  DashboardOverview,
  SeverityDistributionItem,
  ThreatTrendItem,
} from "@/types/dashboard";

export async function getDashboardOverview(): Promise<DashboardOverview> {
  const response = await api.get("/dashboard/overview");
  return response.data;
}

export async function getSeverityDistribution(): Promise<
  SeverityDistributionItem[]
> {
  const response = await api.get("/dashboard/severity-distribution");
  return response.data;
}

export async function getThreatTrend(): Promise<
  ThreatTrendItem[]
> {
  const response = await api.get("/dashboard/threat-trend");
  return response.data;
}

export async function getAlerts() {
  const response = await api.get("/alerts");
  return response.data;
}

export async function getRecentEvents(): Promise<RecentEvent[]> {
  const response = await api.get("/dashboard/events");
  return response.data;
}