import StatCard from "@/components/shared/StatCard";
import {
  ShieldAlert,
  AlertTriangle,
  Activity,
  ShieldCheck,
} from "lucide-react";

interface Props {
  total: number;
  critical: number;
  active: number;
  resolved: number;
}

export default function AlertStats({
  total,
  critical,
  active,
  resolved,
}: Props) {
  return (
    <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="Total Alerts"
        value={total}
        icon={ShieldAlert}
      />

      <StatCard
        title="Critical"
        value={critical}
        icon={AlertTriangle}
        color="text-red-400"
      />

      <StatCard
        title="Active"
        value={active}
        icon={Activity}
        color="text-yellow-400"
      />

      <StatCard
        title="Resolved"
        value={resolved}
        icon={ShieldCheck}
        color="text-green-400"
      />

    </div>
  );
}