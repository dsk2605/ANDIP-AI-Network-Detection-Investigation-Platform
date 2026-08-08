import api from "@/services/api";

import type { Asset } from "../types/asset";

export async function getAssets(): Promise<Asset[]> {
  const response = await api.get("/assets/");

  return response.data;
}