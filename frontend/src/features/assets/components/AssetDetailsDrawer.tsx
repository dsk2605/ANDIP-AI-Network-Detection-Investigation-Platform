import type { Asset } from "../types/asset";

interface Props {
  asset: Asset | null;
  onClose: () => void;
}

export default function AssetDetailsDrawer({
  asset,
  onClose,
}: Props) {
  if (!asset) return null;

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/40">

      <div className="h-full w-[420px] overflow-y-auto border-l border-slate-800 bg-slate-900 p-6">

        <div className="mb-6 flex items-center justify-between">

          <h2 className="text-xl font-semibold text-white">
            Asset Details
          </h2>

          <button
            onClick={onClose}
            className="text-slate-400 transition hover:text-white"
          >
            ✕
          </button>

        </div>

        <div className="space-y-4 text-sm">

          <Detail
            label="Hostname"
            value={asset.hostname}
          />

          <Detail
            label="IP Address"
            value={asset.ip_address}
          />

          <Detail
            label="MAC Address"
            value={asset.mac_address}
          />

          <Detail
            label="Operating System"
            value={asset.operating_system}
          />

          <Detail
            label="Asset Type"
            value={asset.asset_type}
          />

          <Detail
            label="Environment"
            value={asset.environment}
          />

          <Detail
            label="Status"
            value={asset.status}
          />

          <Detail
            label="Risk Score"
            value={asset.risk_score}
          />

          <Detail
            label="Monitored"
            value={
              asset.is_monitored
                ? "Yes"
                : "No"
            }
          />

          <Detail
            label="Last Seen"
            value={
              asset.last_seen ??
              "Never"
            }
          />

        </div>

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
    <div className="border-b border-slate-800 pb-3">

      <p className="mb-1 text-xs uppercase tracking-wider text-slate-500">
        {label}
      </p>

      <p className="text-white">
        {value}
      </p>

    </div>
  );
}