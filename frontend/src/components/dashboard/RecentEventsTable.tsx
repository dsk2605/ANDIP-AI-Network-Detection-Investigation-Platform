import { ShieldAlert, ArrowRight } from "lucide-react";

import Badge from "@/components/ui/Badge";
import { useRecentEvents } from "@/hooks/useDashboard";
import type { RecentEvent } from "@/types/dashboard";

export default function RecentEventsTable() {
  const { data, isLoading, error } = useRecentEvents();

  if (isLoading) {
    return (
      <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
        Loading live threat feed...
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-2xl border border-red-500/20 bg-red-500/10 p-8 text-center text-red-400">
        Failed to load live threat feed.
      </div>
    );
  }

  if (!data || data.length === 0) {
    return (
      <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8 text-center">
        <ShieldAlert
          size={36}
          className="mx-auto mb-3 text-slate-600"
        />

        <h3 className="text-lg font-semibold text-white">
          No Active Threats
        </h3>

        <p className="mt-2 text-sm text-slate-400">
          Your network is currently operating normally.
        </p>
      </div>
    );
  }

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800">

      <table className="min-w-full">

        <thead className="bg-slate-950">

          <tr className="border-b border-slate-800 text-left">

            <th className="px-7 py-5 text-[11px] uppercase tracking-[0.25em] text-slate-500">
              Threat
            </th>

            <th className="px-7 py-5 text-[11px] uppercase tracking-[0.25em] text-slate-500">
              Severity
            </th>

            <th className="px-7 py-5 text-[11px] uppercase tracking-[0.25em] text-slate-500">
              Network Flow
            </th>

            <th className="px-7 py-5 text-[11px] uppercase tracking-[0.25em] text-slate-500">
              Detection Time
            </th>

          </tr>

        </thead>

        <tbody>

          {data.map((event: RecentEvent) => (

            <tr
              key={event.id}
              className="
                border-b
                border-slate-800
                transition-all
                duration-200
                hover:bg-slate-800/30
              "
            >

              <td className="px-7 py-6">

                <div className="flex items-center gap-4">

                  <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-cyan-500/10 text-cyan-400">

                    <ShieldAlert size={20} />

                  </div>

                  <div>

                    <p className="font-semibold text-white">
                      {event.attack}
                    </p>

                    <p className="text-xs text-slate-500">
                      Threat Detected
                    </p>

                  </div>

                </div>

              </td>

              <td className="px-7 py-6">

                <Badge
                  variant={
                    event.severity.toLowerCase() === "critical"
                      ? "critical"
                      : event.severity.toLowerCase() === "high"
                      ? "high"
                      : event.severity.toLowerCase() === "medium"
                      ? "medium"
                      : "low"
                  }
                >
                  {event.severity}
                </Badge>

              </td>

              <td className="px-7 py-6">

                <div className="flex items-center gap-4">

                  <span className="font-mono text-sm text-slate-300">
                    {event.source_ip}
                  </span>

                  <ArrowRight
                    size={16}
                    className="text-slate-600"
                  />

                  <span className="font-mono text-sm text-slate-300">
                    {event.destination_ip}
                  </span>

                </div>

              </td>

              <td className="px-7 py-6">

                <div>

                  <p className="font-medium text-slate-200">
                    {new Date(event.timestamp).toLocaleTimeString()}
                  </p>

                  <p className="text-xs text-slate-500">
                    {new Date(event.timestamp).toLocaleDateString()}
                  </p>

                </div>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}