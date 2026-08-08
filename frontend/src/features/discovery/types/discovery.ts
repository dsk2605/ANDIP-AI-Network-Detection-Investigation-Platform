export interface DiscoveryScan {
  id: string;

  network: string;

  scan_type: string;

  status: "PENDING" | "RUNNING" | "COMPLETED" | "FAILED";

  hosts_found: number;

  started_at: string | null;

  finished_at: string | null;
}