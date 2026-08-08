import DataTable from "@/components/ui/DataTable";

import type { TopRiskAsset } from "../types/analytics";

interface Props {
  assets: TopRiskAsset[];
  isLoading: boolean;
  error: unknown;
}

export default function TopRiskAssetsTable({
  assets,
  isLoading,
  error,
}: Props) {
  return (
    <DataTable
      title="Top 10 Highest Risk Assets"
      isLoading={isLoading}
      error={error}
      emptyMessage="No high-risk assets found."
      columns={
        <tr>
          <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
            Hostname
          </th>

          <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
            IP Address
          </th>

          <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
            Environment
          </th>

          <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
            Asset Type
          </th>

          <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
            Risk
          </th>

          <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-400">
            Status
          </th>
        </tr>
      }
    >
      {assets.map((asset) => {
        let riskClass =
          "bg-green-500/20 text-green-400";
        let riskLabel = "Low";

        if (asset.risk_score >= 80) {
          riskClass =
            "bg-red-500/20 text-red-400";
          riskLabel = "Critical";
        } else if (asset.risk_score >= 60) {
          riskClass =
            "bg-orange-500/20 text-orange-400";
          riskLabel = "High";
        } else if (asset.risk_score >= 40) {
          riskClass =
            "bg-yellow-500/20 text-yellow-400";
          riskLabel = "Medium";
        }

        return (
          <tr
            key={asset.id}
            className="transition-colors hover:bg-slate-800/40"
          >
            <td className="px-6 py-4 font-semibold text-white">
              {asset.hostname}
            </td>

            <td className="px-6 py-4 font-mono text-slate-300">
              {asset.ip_address}
            </td>

            <td className="px-6 py-4 text-slate-300">
              {asset.environment}
            </td>

            <td className="px-6 py-4 text-slate-300">
              {asset.asset_type}
            </td>

            <td className="px-6 py-4">
              <span
                className={`rounded-full px-3 py-1 text-xs font-semibold ${riskClass}`}
              >
                {riskLabel} ({asset.risk_score})
              </span>
            </td>

            <td className="px-6 py-4">
              <span
                className={`rounded-full px-3 py-1 text-xs font-semibold ${
                  asset.status === "ACTIVE"
                    ? "bg-green-500/20 text-green-400"
                    : "bg-slate-700 text-slate-300"
                }`}
              >
                {asset.status}
              </span>
            </td>
          </tr>
        );
      })}
    </DataTable>
  );
}