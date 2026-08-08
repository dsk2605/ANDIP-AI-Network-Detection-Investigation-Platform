import Card from "@/components/ui/Card";

import type { DiscoverySummary } from "../types/analytics";

interface Props {
  summary: DiscoverySummary;
}

export default function DiscoverySummaryCard({
  summary,
}: Props) {

  return (
    <Card className="p-6">

      <h2 className="mb-6 text-lg font-semibold text-white">
        Discovery Summary
      </h2>

      <div className="grid gap-6 sm:grid-cols-2">

        <div>

          <p className="text-sm text-slate-400">
            Total Scans
          </p>

          <p className="mt-1 text-3xl font-bold text-white">
            {summary.total_scans}
          </p>

        </div>

        <div>

          <p className="text-sm text-slate-400">
            Hosts Found
          </p>

          <p className="mt-1 text-3xl font-bold text-cyan-400">
            {summary.total_hosts_discovered}
          </p>

        </div>

        <div>

          <p className="text-sm text-slate-400">
            Avg Hosts / Scan
          </p>

          <p className="mt-1 text-2xl font-semibold text-white">
            {summary.average_hosts_per_scan}
          </p>

        </div>

        <div>

          <p className="text-sm text-slate-400">
            Latest Scan
          </p>

          <p className="mt-1 text-sm text-slate-300">
            {summary.latest_scan
              ? new Date(summary.latest_scan).toLocaleString()
              : "-"}
          </p>

        </div>

      </div>

    </Card>
  );
}