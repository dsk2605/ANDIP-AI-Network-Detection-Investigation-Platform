import { useMemo, useState } from "react";
import { useMutation } from "@tanstack/react-query";

import PageHeader from "@/components/shared/PageHeader";

import DiscoveryStats from "./components/DiscoveryStats";
import DiscoveryToolbar from "./components/DiscoveryToolbar";
import DiscoveryTable from "./components/DiscoveryTable";
import DiscoveryDetailsDrawer from "./components/DiscoveryDetailsDrawer";
import StartScanDialog from "./components/StartScanDialog";

import { useDiscovery } from "./hooks/useDiscovery";

import {
  startDiscoveryScan,
} from "./services/discovery";

import type { DiscoveryScan } from "./types/discovery";

export default function DiscoveryPage() {
  const [search, setSearch] = useState("");
  const [status, setStatus] = useState("");

  const [selectedScan, setSelectedScan] =
    useState<DiscoveryScan | null>(null);

  const [scanDialogOpen, setScanDialogOpen] =
    useState(false);

  const {
    data,
    isLoading,
    isFetching,
    error,
    refetch,
  } = useDiscovery();

  const scanMutation = useMutation({
    mutationFn: startDiscoveryScan,

    onSuccess: async () => {
      setScanDialogOpen(false);
      await refetch();
    },
  });

  const filteredScans = useMemo(() => {
    if (!data) return [];

    return data.filter((scan) => {
      const matchesSearch =
        scan.network
          .toLowerCase()
          .includes(search.toLowerCase());

      const matchesStatus =
        status === "" ||
        scan.status === status;

      return (
        matchesSearch &&
        matchesStatus
      );
    });
  }, [data, search, status]);

  return (
    <div className="space-y-8">

      <PageHeader
        title="Network Discovery"
        subtitle="Discover and monitor network scan history"
      />

      <DiscoveryStats
        scans={filteredScans}
      />

      <DiscoveryToolbar
        search={search}
        onSearchChange={setSearch}
        status={status}
        onStatusChange={setStatus}
        onRefresh={refetch}
        onExport={() => {}}
        onStartScan={() =>
          setScanDialogOpen(true)
        }
        isRefreshing={isFetching}
      />

      <DiscoveryTable
        scans={filteredScans}
        isLoading={isLoading}
        error={error}
        onSelectScan={setSelectedScan}
      />

      <DiscoveryDetailsDrawer
        scan={selectedScan}
        onClose={() =>
          setSelectedScan(null)
        }
      />

      <StartScanDialog
        open={scanDialogOpen}
        loading={scanMutation.isPending}
        onClose={() =>
          setScanDialogOpen(false)
        }
        onStart={(target) =>
          scanMutation.mutate({
            target,
          })
        }
      />

    </div>
  );
}