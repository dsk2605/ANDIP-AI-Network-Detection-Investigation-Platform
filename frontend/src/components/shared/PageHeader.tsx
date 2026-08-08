import { Activity, Clock3, ShieldCheck } from "lucide-react";

interface PageHeaderProps {
  title: string;
  subtitle: string;
}

export default function PageHeader({
  title,
  subtitle,
}: PageHeaderProps) {
  const now = new Date().toLocaleString([], {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    day: "2-digit",
    month: "short",
  });

  return (
    <header className="mb-10 border-b border-slate-800 pb-7">

      <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

        <div>

          <div className="mb-3 inline-flex items-center gap-2 rounded-full border border-emerald-500/20 bg-emerald-500/10 px-3 py-1">

            <ShieldCheck
              size={14}
              className="text-emerald-400"
            />

            <span className="text-xs font-medium tracking-wide text-emerald-400">
              SYSTEM OPERATIONAL
            </span>

          </div>

          <h1 className="text-4xl font-bold tracking-tight text-white">
            {title}
          </h1>

          <p className="mt-3 max-w-2xl text-sm leading-6 text-slate-400">
            {subtitle}
          </p>

        </div>

        <div className="min-w-[260px] rounded-2xl border border-slate-800 bg-slate-900/70 p-5">

          <div className="flex items-center justify-between">

            <span className="text-xs font-semibold uppercase tracking-widest text-slate-500">
              Status
            </span>

            <div className="flex items-center gap-2">

              <div className="h-2.5 w-2.5 rounded-full bg-emerald-400 animate-pulse" />

              <span className="text-sm font-medium text-emerald-400">
                Monitoring Active
              </span>

            </div>

          </div>

          <div className="mt-5 flex items-center gap-2 text-sm text-slate-400">

            <Clock3 size={15} />

            <span>
              Last Updated
            </span>

            <span className="font-medium text-slate-300">
              {now}
            </span>

          </div>

          <div className="mt-3 flex items-center gap-2 text-sm text-slate-400">

            <Activity
              size={15}
              className="text-cyan-400"
            />

            <span>
              Live telemetry stream connected
            </span>

          </div>

        </div>

      </div>

    </header>
  );
}