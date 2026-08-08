import api from "@/services/api";

import type { AlertsResponse } from "../types/alert";

export async function getAlerts(
  page = 1,
  limit = 25,
): Promise<AlertsResponse> {
  const response = await api.get("/alerts", {
    params: {
      page,
      limit,
    },
  });

  return response.data;
}