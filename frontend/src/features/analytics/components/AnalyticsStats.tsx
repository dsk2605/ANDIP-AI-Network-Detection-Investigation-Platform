import {
  AlertTriangle,
  Monitor,
  Search,
  Shield,
} from "lucide-react";

import StatCard from "@/components/shared/StatCard";

import type { AnalyticsSummary } from "../types/analytics";

interface Props {
  analytics?: AnalyticsSummary;
}

export default function AnalyticsStats({
  analytics,
}: Props) {
  return (
    <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="Total Alerts"
        value={analytics?.totalAlerts ?? 0}
        icon={AlertTriangle}
        color="text-red-400"
      />

      <StatCard
        title="Assets"
        value={analytics?.totalAssets ?? 0}
        icon={Monitor}
        color="text-cyan-400"
      />

      <StatCard
        title="Scans"
        value={analytics?.totalScans ?? 0}
        icon={Search}
        color="text-blue-400"
      />

      <StatCard
        title="Average Risk"
        value={analytics?.averageRiskScore ?? 0}
        icon={Shield}
        color="text-amber-400"
      />

    </div>
  );
}