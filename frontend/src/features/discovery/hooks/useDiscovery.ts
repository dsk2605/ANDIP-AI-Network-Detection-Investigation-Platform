import { useQuery } from "@tanstack/react-query";

import { getDiscoveryScans } from "../services/discovery";

export function useDiscovery() {
  return useQuery({
    queryKey: ["discovery-scans"],
    queryFn: getDiscoveryScans,
    refetchInterval: 5000,
  });
}