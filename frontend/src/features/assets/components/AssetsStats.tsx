import {
  Activity,
  Monitor,
  Server,
  ShieldAlert,
} from "lucide-react";

import StatCard from "@/components/shared/StatCard";

import type { Asset } from "../types/asset";

interface Props {
  assets: Asset[];
}

export default function AssetsStats({
  assets,
}: Props) {
  const total = assets.length;

  const active = assets.filter(
    (asset) => asset.status === "ACTIVE"
  ).length;

  const monitored = assets.filter(
    (asset) => asset.is_monitored
  ).length;

  const critical = assets.filter(
    (asset) => asset.risk_score >= 80
  ).length;

  return (
    <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="Total Assets"
        value={total}
        icon={Server}
      />

      <StatCard
        title="Active"
        value={active}
        icon={Activity}
        color="text-green-400"
      />

      <StatCard
        title="Monitored"
        value={monitored}
        icon={Monitor}
        color="text-cyan-400"
      />

      <StatCard
        title="Critical"
        value={critical}
        icon={ShieldAlert}
        color="text-red-400"
      />

    </div>
  );
}