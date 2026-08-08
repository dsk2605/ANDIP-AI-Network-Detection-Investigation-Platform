import { useQuery } from "@tanstack/react-query";

import { getAlerts } from "../services/alerts";

export function useAlerts(
  page = 1,
  limit = 25,
) {
  return useQuery({
    queryKey: ["alerts", page, limit],
    queryFn: () => getAlerts(page, limit),
    refetchInterval: 5000,
  });
}