import { ShieldAlert } from "lucide-react";

import DataTable from "@/components/ui/DataTable";
import SeverityBadge from "./SeverityBadge";

import type { Alert } from "../types/alert";

interface Props {
  alerts: Alert[];
  isLoading: boolean;
  error: unknown;
  onSelectAlert: (alert: Alert) => void;
}

export default function AlertsTable({
  alerts,
  isLoading,
  error,
  onSelectAlert,
}: Props) {
  if (isLoading) {
    return (
      <div className="rounded-xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
        Loading alerts...
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-xl border border-red-900 bg-red-950/30 p-8 text-center text-red-400">
        Failed to load alerts.
      </div>
    );
  }

  if (alerts.length === 0) {
    return (
      <div className="rounded-xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
        No matching alerts found.
      </div>
    );
  }

  return (
    <DataTable
      columns={
        <tr className="text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
          <th className="px-6 py-4">Attack</th>
          <th className="px-6 py-4">Severity</th>
          <th className="px-6 py-4">Source IP</th>
          <th className="px-6 py-4">Destination IP</th>
          <th className="px-6 py-4">Detected</th>
        </tr>
      }
    >
      {alerts.map((alert) => (
        <tr
          key={alert.id}
          onClick={() => onSelectAlert(alert)}
          className="
            cursor-pointer
            transition-all
            duration-200
            hover:bg-slate-800/40
            hover:shadow-inner
          "
        >
          <td className="px-6 py-4">
            <div className="flex items-center gap-3">
              <ShieldAlert
                size={18}
                className="text-cyan-400"
              />

              <span className="font-medium text-white">
                {alert.attack}
              </span>
            </div>
          </td>

          <td className="px-6 py-4">
            <SeverityBadge severity={alert.severity} />
          </td>

          <td className="px-6 py-4 font-mono text-sm text-slate-300">
            {alert.source_ip}
          </td>

          <td className="px-6 py-4 font-mono text-sm text-slate-300">
            {alert.destination_ip}
          </td>

          <td className="px-6 py-4 text-sm text-slate-400">
            {new Date(alert.timestamp).toLocaleString()}
          </td>
        </tr>
      ))}
    </DataTable>
  );
}