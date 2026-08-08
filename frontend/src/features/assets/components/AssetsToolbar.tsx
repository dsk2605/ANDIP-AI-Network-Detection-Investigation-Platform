import { Download, RotateCw } from "lucide-react";

import SearchInput from "@/components/ui/SearchInput";

interface Props {
  search: string;
  onSearchChange: (value: string) => void;

  status: string;
  onStatusChange: (value: string) => void;

  onRefresh: () => void;

  onExport: () => void;

  isRefreshing: boolean;
}

export default function AssetsToolbar({
  search,
  onSearchChange,
  status,
  onStatusChange,
  onRefresh,
  onExport,
  isRefreshing,
}: Props) {
  return (
    <div className="mb-6 flex flex-wrap items-center justify-between gap-4 rounded-xl border border-slate-800 bg-slate-900 p-4">

      <SearchInput
        value={search}
        onChange={onSearchChange}
        placeholder="Search hostname or IP..."
      />

      <div className="flex items-center gap-3">

        <select
          value={status}
          onChange={(e) => onStatusChange(e.target.value)}
          className="rounded-lg border border-slate-700 bg-slate-950 px-4 py-2 text-sm text-white outline-none transition focus:border-cyan-500"
        >
          <option value="">All Status</option>
          <option value="ACTIVE">Active</option>
          <option value="INACTIVE">Inactive</option>
          <option value="UNKNOWN">Unknown</option>
        </select>

        <button
          onClick={onRefresh}
          disabled={isRefreshing}
          className="flex items-center gap-2 rounded-lg border border-slate-700 bg-slate-950 px-4 py-2 text-sm text-slate-300 transition hover:border-cyan-500 hover:text-white disabled:opacity-50"
        >
          <RotateCw
            size={16}
            className={isRefreshing ? "animate-spin" : ""}
          />

          {isRefreshing ? "Refreshing..." : "Refresh"}
        </button>

        <button
          onClick={onExport}
          className="flex items-center gap-2 rounded-lg border border-slate-700 bg-slate-950 px-4 py-2 text-sm text-slate-300 transition hover:border-cyan-500 hover:text-white"
        >
          <Download size={16} />
          Export
        </button>

      </div>

    </div>
  );
}