import { Monitor } from "lucide-react";

import DataTable from "@/components/ui/DataTable";

import AssetStatusBadge from "./AssetStatusBadge";

import type { Asset } from "../types/asset";

interface Props {
  assets: Asset[];
  isLoading: boolean;
  error: unknown;

  onSelectAsset: (asset: Asset) => void;
}

export default function AssetsTable({
  assets,
  isLoading,
  error,
  onSelectAsset,
}: Props) {
  if (isLoading) {
    return (
      <div className="rounded-xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
        Loading assets...
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-xl border border-red-900 bg-red-950/30 p-8 text-center text-red-400">
        Failed to load assets.
      </div>
    );
  }

  if (assets.length === 0) {
    return (
      <div className="rounded-xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
        No assets found.
      </div>
    );
  }

  return (
    <DataTable
      columns={
        <tr className="text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
          <th className="px-6 py-4">Hostname</th>
          <th className="px-6 py-4">IP Address</th>
          <th className="px-6 py-4">Operating System</th>
          <th className="px-6 py-4">Risk</th>
          <th className="px-6 py-4">Status</th>
        </tr>
      }
    >
      {assets.map((asset) => (
        <tr
          key={asset.id}
          onClick={() => onSelectAsset(asset)}
          className="cursor-pointer transition-colors hover:bg-slate-800/40"
        >
          <td className="px-6 py-4">
            <div className="flex items-center gap-3">
              <Monitor
                size={18}
                className="text-cyan-400"
              />

              <span className="font-medium text-white">
                {asset.hostname}
              </span>
            </div>
          </td>

          <td className="px-6 py-4 font-mono text-sm text-slate-300">
            {asset.ip_address}
          </td>

          <td className="px-6 py-4 text-slate-300">
            {asset.operating_system}
          </td>

          <td className="px-6 py-4">
            <span
              className={`font-semibold ${
                asset.risk_score >= 80
                  ? "text-red-400"
                  : asset.risk_score >= 60
                  ? "text-yellow-400"
                  : "text-green-400"
              }`}
            >
              {asset.risk_score}
            </span>
          </td>

          <td className="px-6 py-4">
            <AssetStatusBadge
              status={asset.status}
            />
          </td>
        </tr>
      ))}
    </DataTable>
  );
}