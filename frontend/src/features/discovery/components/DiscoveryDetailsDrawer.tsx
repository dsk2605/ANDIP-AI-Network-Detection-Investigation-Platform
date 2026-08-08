import type { DiscoveryScan } from "../types/discovery";

interface Props {
  scan: DiscoveryScan | null;
  onClose: () => void;
}

export default function DiscoveryDetailsDrawer({
  scan,
  onClose,
}: Props) {
  if (!scan) return null;

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/40">

      <div className="h-full w-[420px] overflow-y-auto border-l border-slate-800 bg-slate-900 p-6">

        <div className="mb-6 flex items-center justify-between">

          <h2 className="text-xl font-semibold text-white">
            Discovery Details
          </h2>

          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white"
          >
            ✕
          </button>

        </div>

        <Detail
          label="Network"
          value={scan.network}
        />

        <Detail
          label="Status"
          value={scan.status}
        />

        <Detail
          label="Scan Type"
          value={scan.scan_type}
        />

        <Detail
          label="Hosts Found"
          value={scan.hosts_found}
        />

        <Detail
          label="Started"
          value={
            scan.started_at
              ? new Date(scan.started_at).toLocaleString()
              : "-"
          }
        />

        <Detail
          label="Finished"
          value={
            scan.finished_at
              ? new Date(scan.finished_at).toLocaleString()
              : "-"
          }
        />

      </div>

    </div>
  );
}

function Detail({
  label,
  value,
}: {
  label: string;
  value: React.ReactNode;
}) {
  return (
    <div className="border-b border-slate-800 py-3">

      <p className="mb-1 text-xs uppercase tracking-wider text-slate-500">
        {label}
      </p>

      <p className="text-white">
        {value}
      </p>

    </div>
  );
}