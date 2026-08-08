import type { Alert } from "../types/alert";

export function exportAlertsAsJson(alerts: Alert[]) {
  const blob = new Blob(
    [JSON.stringify(alerts, null, 2)],
    {
      type: "application/json",
    }
  );

  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;
  link.download = `alerts-${Date.now()}.json`;

  link.click();

  URL.revokeObjectURL(url);
}

export function exportAlertsAsCsv(alerts: Alert[]) {
  const headers = [
    "Attack",
    "Severity",
    "Source IP",
    "Destination IP",
    "Timestamp",
    "Description",
  ];

  const rows = alerts.map((alert) => [
    alert.attack,
    alert.severity,
    alert.source_ip,
    alert.destination_ip,
    alert.timestamp,
    alert.description,
  ]);

  const csv = [
    headers,
    ...rows,
  ]
    .map((row) => row.join(","))
    .join("\n");

  const blob = new Blob(
    [csv],
    {
      type: "text/csv",
    }
  );

  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;
  link.download = `alerts-${Date.now()}.csv`;

  link.click();

  URL.revokeObjectURL(url);
}