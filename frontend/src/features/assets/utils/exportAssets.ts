import type { Asset } from "../types/asset";

export function exportAssetsAsCsv(assets: Asset[]) {
  const headers = [
    "Hostname",
    "IP Address",
    "MAC Address",
    "Operating System",
    "Asset Type",
    "Environment",
    "Status",
    "Risk Score",
    "Monitored",
    "Last Seen",
  ];

  const rows = assets.map((asset) => [
    asset.hostname,
    asset.ip_address,
    asset.mac_address,
    asset.operating_system,
    asset.asset_type,
    asset.environment,
    asset.status,
    asset.risk_score,
    asset.is_monitored ? "Yes" : "No",
    asset.last_seen ?? "Never",
  ]);

  const csv = [
    headers.join(","),
    ...rows.map((row) => row.join(",")),
  ].join("\n");

  const blob = new Blob([csv], {
    type: "text/csv;charset=utf-8;",
  });

  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;
  link.download = "assets.csv";

  link.click();

  URL.revokeObjectURL(url);
}