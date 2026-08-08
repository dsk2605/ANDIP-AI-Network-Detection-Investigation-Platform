import { Radar } from "lucide-react";

import DataTable from "@/components/ui/DataTable";

import DiscoveryStatusBadge from "./DiscoveryStatusBadge";

import type { DiscoveryScan } from "../types/discovery";

interface Props {
  scans: DiscoveryScan[];
  isLoading: boolean;
  error: unknown;

  onSelectScan: (scan: DiscoveryScan) => void;
}

export default function DiscoveryTable({
  scans,
  isLoading,
  error,
  onSelectScan,
}: Props) {
  if (isLoading) {
    return (
      <div className="rounded-xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
        Loading discovery scans...
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-xl border border-red-900 bg-red-950/30 p-8 text-center text-red-400">
        Failed to load discovery scans.
      </div>
    );
  }

  if (scans.length === 0) {
    return (
      <div className="rounded-xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
        No discovery scans found.
      </div>
    );
  }

  return (
    <DataTable
      columns={
        <tr className="text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
          <th className="px-6 py-4">Network</th>
          <th className="px-6 py-4">Status</th>
          <th className="px-6 py-4">Hosts</th>
          <th className="px-6 py-4">Started</th>
          <th className="px-6 py-4">Finished</th>
        </tr>
      }
    >
      {scans.map((scan) => (
        <tr
          key={scan.id}
          onClick={() => onSelectScan(scan)}
          className="cursor-pointer transition-colors hover:bg-slate-800/40"
        >
          <td className="px-6 py-4">
            <div className="flex items-center gap-3">
              <Radar
                size={18}
                className="text-cyan-400"
              />

              <span className="font-medium text-white">
                {scan.network}
              </span>
            </div>
          </td>

          <td className="px-6 py-4">
            <DiscoveryStatusBadge
              status={scan.status}
            />
          </td>

          <td className="px-6 py-4 text-slate-300">
            {scan.hosts_found}
          </td>

          <td className="px-6 py-4 text-slate-400 text-sm">
            {scan.started_at
              ? new Date(scan.started_at).toLocaleString()
              : "-"}
          </td>

          <td className="px-6 py-4 text-slate-400 text-sm">
            {scan.finished_at
              ? new Date(scan.finished_at).toLocaleString()
              : "-"}
          </td>
        </tr>
      ))}
    </DataTable>
  );
}