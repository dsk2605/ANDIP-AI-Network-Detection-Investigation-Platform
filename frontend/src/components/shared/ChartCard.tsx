import type { ReactNode } from "react";
import { Activity } from "lucide-react";

import Card from "@/components/ui/Card";

interface ChartCardProps {
  title: string;
  subtitle?: string;
  children: ReactNode;
}

export default function ChartCard({
  title,
  subtitle,
  children,
}: ChartCardProps) {
  return (
    <Card className="overflow-hidden">

      {/* Header */}

      <div className="flex items-center justify-between border-b border-slate-800 px-7 py-6">

        <div>

          <p className="text-[11px] font-bold uppercase tracking-[0.28em] text-slate-500">
            Threat Intelligence
          </p>

          <h3 className="mt-2 text-2xl font-bold text-white">
            {title}
          </h3>

          {subtitle && (
            <p className="mt-1 text-sm text-slate-400">
              {subtitle}
            </p>
          )}

        </div>

        <div className="flex items-center gap-2 rounded-full border border-emerald-500/20 bg-emerald-500/10 px-4 py-2">

          <Activity
            size={16}
            className="text-emerald-400"
          />

          <span className="text-xs font-semibold uppercase tracking-wider text-emerald-400">
            LIVE
          </span>

        </div>

      </div>

      {/* Chart */}

      <div className="h-[420px] px-4 py-4">
        {children}
      </div>

      {/* Footer */}

      <div className="flex items-center justify-between border-t border-slate-800 bg-slate-950/40 px-7 py-4">

        <span className="text-xs uppercase tracking-[0.18em] text-slate-500">
          Auto Refresh • 5 Seconds
        </span>

        <span className="text-xs font-semibold text-cyan-400">
          Live Network Telemetry
        </span>

      </div>

    </Card>
  );
}