import { useMemo, useState } from "react";

import PageHeader from "@/components/shared/PageHeader";

import AssetsStats from "./components/AssetsStats";
import AssetsToolbar from "./components/AssetsToolbar";
import AssetsTable from "./components/AssetsTable";
import AssetDetailsDrawer from "./components/AssetDetailsDrawer";

import { useAssets } from "./hooks/useAssets";
import { exportAssetsAsCsv } from "./utils/exportAssets";

import type { Asset } from "./types/asset";

export default function AssetsPage() {
  const [search, setSearch] = useState("");
  const [status, setStatus] = useState("");

  const [selectedAsset, setSelectedAsset] =
    useState<Asset | null>(null);

  const {
    data,
    isLoading,
    isFetching,
    error,
    refetch,
  } = useAssets();

  const filteredAssets = useMemo(() => {
    if (!data) return [];

    return data.filter((asset) => {
      const matchesSearch =
        asset.hostname
          .toLowerCase()
          .includes(search.toLowerCase()) ||
        asset.ip_address.includes(search);

      const matchesStatus =
        status === "" ||
        asset.status === status;

      return matchesSearch && matchesStatus;
    });
  }, [data, search, status]);

  return (
    <div className="space-y-8">

      <PageHeader
        title="Assets"
        subtitle="Monitor and manage all discovered assets"
      />

      <AssetsStats
        assets={filteredAssets}
      />

      <AssetsToolbar
        search={search}
        onSearchChange={setSearch}
        status={status}
        onStatusChange={setStatus}
        onRefresh={refetch}
        onExport={() => exportAssetsAsCsv(filteredAssets)}
        isRefreshing={isFetching}
      />

      <AssetsTable
        assets={filteredAssets}
        isLoading={isLoading}
        error={error}
        onSelectAsset={setSelectedAsset}
      />

      <AssetDetailsDrawer
        asset={selectedAsset}
        onClose={() => setSelectedAsset(null)}
      />

    </div>
  );
}