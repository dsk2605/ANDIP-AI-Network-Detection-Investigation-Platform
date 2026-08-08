import { useEffect, useMemo, useState } from "react";

import PageHeader from "@/components/shared/PageHeader";

import AlertStats from "./components/AlertStats";
import AlertDetailsDrawer from "./components/AlertDetailsDrawer";
import AlertsToolbar from "./components/AlertsToolbar";
import AlertsTable from "./components/AlertsTable";
import LiveStatus from "./components/LiveStatus";
import Pagination from "./components/Pagination";

import { useAlerts } from "./hooks/useAlerts";
import { exportAlertsAsCsv } from "./utils/exportAlerts";

import type { Alert } from "./types/alert";

export default function AlertsPage() {
  const [page, setPage] = useState(1);

  const [search, setSearch] = useState("");
  const [severity, setSeverity] = useState("");

  const [selectedAlert, setSelectedAlert] =
    useState<Alert | null>(null);

  const [lastUpdated, setLastUpdated] =
    useState(new Date());

  const {
    data,
    isLoading,
    isFetching,
    error,
    refetch,
  } = useAlerts(page, 25);

  useEffect(() => {
    if (data) {
      setLastUpdated(new Date());
    }
  }, [data]);

  const filteredAlerts = useMemo(() => {
    if (!data) return [];

    return data.items.filter((alert) => {
      const matchesSearch =
        alert.attack
          .toLowerCase()
          .includes(search.toLowerCase()) ||
        alert.source_ip.includes(search) ||
        alert.destination_ip.includes(search);

      const matchesSeverity =
        severity === "" ||
        alert.severity === severity;

      return matchesSearch && matchesSeverity;
    });
  }, [data, search, severity]);

  return (
    <div className="space-y-8">

      <PageHeader
        title="Security Alerts"
        subtitle="Monitor, investigate and respond to security events"
      />

      <LiveStatus
        lastUpdated={lastUpdated}
      />

      <AlertStats
        total={data?.total ?? 0}
        critical={
          filteredAlerts.filter(
            (alert) =>
              alert.severity === "Critical"
          ).length
        }
        active={filteredAlerts.length}
        resolved={0}
      />

      <AlertsToolbar
        search={search}
        onSearchChange={setSearch}
        severity={severity}
        onSeverityChange={setSeverity}
        onRefresh={() => {
          refetch();
          setLastUpdated(new Date());
        }}
        onExport={() =>
          exportAlertsAsCsv(filteredAlerts)
        }
        isRefreshing={isFetching}
      />

      <AlertsTable
        alerts={filteredAlerts}
        isLoading={isLoading}
        error={error}
        onSelectAlert={setSelectedAlert}
      />

      <Pagination
        page={page}
        pages={data?.pages ?? 1}
        onPrevious={() =>
          setPage((prev) =>
            Math.max(1, prev - 1)
          )
        }
        onNext={() =>
          setPage((prev) =>
            Math.min(
              data?.pages ?? 1,
              prev + 1
            )
          )
        }
      />

      <AlertDetailsDrawer
        alert={selectedAlert}
        onClose={() =>
          setSelectedAlert(null)
        }
      />

    </div>
  );
}