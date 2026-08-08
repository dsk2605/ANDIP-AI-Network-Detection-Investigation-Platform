import {
  Radar,
  CheckCircle2,
  LoaderCircle,
  XCircle,
} from "lucide-react";

import StatCard from "@/components/shared/StatCard";

import type { DiscoveryScan } from "../types/discovery";

interface Props {
  scans: DiscoveryScan[];
}

export default function DiscoveryStats({
  scans,
}: Props) {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="Total Scans"
        value={scans.length}
        icon={Radar}
      />

      <StatCard
        title="Completed"
        value={
          scans.filter(
            (scan) => scan.status === "COMPLETED"
          ).length
        }
        icon={CheckCircle2}
      />

      <StatCard
        title="Running"
        value={
          scans.filter(
            (scan) => scan.status === "RUNNING"
          ).length
        }
        icon={LoaderCircle}
      />

      <StatCard
        title="Failed"
        value={
          scans.filter(
            (scan) => scan.status === "FAILED"
          ).length
        }
        icon={XCircle}
      />

    </div>
  );
}