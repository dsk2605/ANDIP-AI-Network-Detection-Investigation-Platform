import api from "@/services/api";

import type { DiscoveryScan } from "../types/discovery";

export interface StartDiscoveryScanRequest {
  target: string;
}

export interface StartDiscoveryScanResponse {
  message: string;
  scan_id: string;
  assets_discovered: number;
}

export async function getDiscoveryScans(): Promise<DiscoveryScan[]> {
  const response = await api.get("/discovery/scans");

  return response.data;
}

export async function startDiscoveryScan(
  payload: StartDiscoveryScanRequest,
): Promise<StartDiscoveryScanResponse> {
  const response = await api.post(
    "/discovery/scan",
    payload,
  );

  return response.data;
}