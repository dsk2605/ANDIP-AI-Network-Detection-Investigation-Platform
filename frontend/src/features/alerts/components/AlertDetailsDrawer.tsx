import SeverityBadge from "./SeverityBadge";
import type { Alert } from "../types/alert";

interface Props {
  alert: Alert | null;
  onClose: () => void;
}

export default function AlertDetailsDrawer({
  alert,
  onClose,
}: Props) {
  if (!alert) return null;

  const details = alert.details as {
    ports_scanned?: number;
    ports?: number[];
  };

  return (
    <div className="fixed inset-y-0 right-0 z-50 w-[460px] overflow-y-auto border-l border-slate-800 bg-slate-950 shadow-2xl">

      {/* Header */}

      <div className="sticky top-0 border-b border-slate-800 bg-slate-950 px-6 py-5">

        <div className="flex items-center justify-between">

          <div>

            <h2 className="text-lg font-semibold text-white">
              Alert Investigation
            </h2>

            <p className="mt-1 text-sm text-slate-400">
              Security Event Details
            </p>

          </div>

          <button
            onClick={onClose}
            className="rounded-lg px-2 py-1 text-slate-400 transition hover:bg-slate-800 hover:text-white"
          >
            ✕
          </button>

        </div>

      </div>

      <div className="space-y-8 p-6">

        {/* General */}

        <section>

          <h3 className="mb-4 text-xs font-semibold uppercase tracking-wider text-slate-500">
            General
          </h3>

          <Info
            label="Attack"
            value={alert.attack}
          />

          <div className="mt-4">
            <p className="mb-2 text-xs uppercase tracking-wide text-slate-500">
              Severity
            </p>

            <SeverityBadge severity={alert.severity} />
          </div>

          <Info
            label="Description"
            value={alert.description}
          />

        </section>

        {/* Network */}

        <section>

          <h3 className="mb-4 text-xs font-semibold uppercase tracking-wider text-slate-500">
            Network
          </h3>

          <Info
            label="Source IP"
            value={alert.source_ip}
          />

          <Info
            label="Destination IP"
            value={alert.destination_ip}
          />

        </section>

        {/* Detection */}

        <section>

          <h3 className="mb-4 text-xs font-semibold uppercase tracking-wider text-slate-500">
            Detection
          </h3>

          <Info
            label="Timestamp"
            value={new Date(alert.timestamp).toLocaleString()}
          />

          <Info
            label="Ports Scanned"
            value={String(details.ports_scanned ?? "-")}
          />

        </section>

        {/* Evidence */}

        <section>

          <h3 className="mb-4 text-xs font-semibold uppercase tracking-wider text-slate-500">
            Evidence
          </h3>

          <div className="rounded-lg border border-slate-800 bg-slate-900 p-4">

            <div className="flex flex-wrap gap-2">

              {details.ports?.map((port) => (
                <span
                  key={port}
                  className="rounded-md bg-slate-800 px-3 py-1 text-xs font-medium text-cyan-400"
                >
                  {port}
                </span>
              ))}

            </div>

          </div>

        </section>

        {/* Recommended Action */}

        <section>

          <h3 className="mb-4 text-xs font-semibold uppercase tracking-wider text-slate-500">
            Recommended Action
          </h3>

          <div className="rounded-lg border border-yellow-700/30 bg-yellow-900/10 p-4">

            <p className="text-sm leading-6 text-slate-300">
              Review the originating host, validate whether the activity
              was authorized, and investigate the scanned ports for
              exposed services or unusual behavior.
            </p>

          </div>

        </section>

      </div>

    </div>
  );
}

function Info({
  label,
  value,
}: {
  label: string;
  value: string;
}) {
  return (
    <div className="mb-4">

      <p className="mb-1 text-xs uppercase tracking-wide text-slate-500">
        {label}
      </p>

      <p className="break-all text-sm text-white">
        {value}
      </p>

    </div>
  );
}