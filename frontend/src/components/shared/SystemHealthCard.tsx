import {
  Activity,
  Database,
  Server,
  ShieldCheck,
  Radio,
  Boxes,
} from "lucide-react";

import Card from "@/components/ui/Card";
import StatusIndicator from "@/components/ui/StatusIndicator";

const services = [
  {
    icon: Server,
    label: "Backend API",
    status: "online",
    description: "FastAPI services operational",
  },
  {
    icon: Database,
    label: "PostgreSQL",
    status: "online",
    description: "Database connection healthy",
  },
  {
    icon: Boxes,
    label: "Docker Services",
    status: "online",
    description: "Containers running",
  },
  {
    icon: Radio,
    label: "WebSocket",
    status: "online",
    description: "Real-time event streaming",
  },
  {
    icon: Activity,
    label: "Packet Collector",
    status: "online",
    description: "Capturing live network traffic",
  },
  {
    icon: ShieldCheck,
    label: "Detection Engine",
    status: "online",
    description: "Threat analysis active",
  },
] as const;

export default function SystemHealthCard() {
  return (
    <Card className="overflow-hidden">

      {/* Header */}

      <div className="flex items-center justify-between border-b border-slate-800 px-7 py-6">

        <div>

          <p className="text-[11px] font-bold uppercase tracking-[0.28em] text-slate-500">
            Infrastructure Health
          </p>

          <h3 className="mt-2 text-xl font-bold text-white">
            Core Platform Services
          </h3>

          <p className="mt-1 text-sm text-slate-400">
            Live operational status of ANDIP components
          </p>

        </div>

        <div className="rounded-full border border-emerald-500/20 bg-emerald-500/10 px-4 py-2">

          <span className="text-xs font-semibold uppercase tracking-wider text-emerald-400">
            All Systems Operational
          </span>

        </div>

      </div>

      {/* Services */}

      <div className="divide-y divide-slate-800">

        {services.map((service) => {
          const Icon = service.icon;

          return (
            <div
              key={service.label}
              className="
                flex
                items-center
                justify-between
                px-7
                py-5
                transition-all
                duration-200
                hover:bg-slate-800/30
              "
            >

              <div className="flex items-center gap-4">

                <div
                  className="
                    flex
                    h-12
                    w-12
                    items-center
                    justify-center
                    rounded-2xl
                    border
                    border-slate-700
                    bg-slate-800/70
                    text-cyan-400
                  "
                >
                  <Icon size={20} />
                </div>

                <div>

                  <p className="font-semibold text-white">
                    {service.label}
                  </p>

                  <p className="text-xs text-slate-500">
                    {service.description}
                  </p>

                </div>

              </div>

              <StatusIndicator
                label=""
                status={service.status}
              />

            </div>
          );
        })}

      </div>

      {/* Footer */}

      <div className="flex items-center justify-between border-t border-slate-800 bg-slate-950/40 px-7 py-5">

        <div>

          <p className="text-xs uppercase tracking-[0.25em] text-slate-500">
            Overall Platform Status
          </p>

          <p className="mt-1 text-sm text-slate-400">
            All monitored services are functioning normally.
          </p>

        </div>

        <div className="text-right">

          <p className="text-2xl font-bold text-emerald-400">
            100%
          </p>

          <p className="text-xs uppercase tracking-wider text-slate-500">
            Operational
          </p>

        </div>

      </div>

    </Card>
  );
}