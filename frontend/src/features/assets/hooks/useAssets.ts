import { useQuery } from "@tanstack/react-query";

import { getAssets } from "../services/assets";

export function useAssets() {
  return useQuery({
    queryKey: ["assets"],
    queryFn: getAssets,
    refetchInterval: 5000,
  });
}