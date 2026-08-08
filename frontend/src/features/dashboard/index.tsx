import {
  Activity,
  AlertTriangle,
  Globe,
  ShieldAlert,
} from "lucide-react";

import ThreatTrendChart from "@/components/charts/ThreatTrendChart";
import SeverityChart from "@/components/charts/SeverityChart";

import RecentEventsTable from "@/components/dashboard/RecentEventsTable";

import ChartCard from "@/components/shared/ChartCard";
import PageHeader from "@/components/shared/PageHeader";
import StatCard from "@/components/shared/StatCard";
import SystemHealthCard from "@/components/shared/SystemHealthCard";
import SectionHeader from "@/components/ui/SectionHeader";

import { useDashboardOverview } from "@/hooks/useDashboard";

export default function DashboardPage() {
  const { data, isLoading, error } = useDashboardOverview();

  if (isLoading) {
    return (
      <div className="flex h-[60vh] items-center justify-center text-slate-400">
        Loading Dashboard...
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="flex h-[60vh] items-center justify-center text-red-400">
        Failed to connect to the backend.
      </div>
    );
  }

  return (
    <div className="space-y-8">

      {/* ===================== PAGE HEADER ===================== */}

      <PageHeader
        title="Security Operations Center"
        subtitle="Real-Time Network Detection & Investigation Platform"
      />

      {/* ===================== EXECUTIVE OVERVIEW ===================== */}

      <section className="space-y-5">

        <SectionHeader
          title="Executive Overview"
          subtitle="Live security posture and operational metrics"
        />

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

          <StatCard
            title="Total Alerts"
            value={data.total_alerts}
            icon={ShieldAlert}
          />

          <StatCard
            title="Critical Alerts"
            value={data.critical}
            icon={AlertTriangle}
            color="text-red-400"
          />

          <StatCard
            title="Today's Alerts"
            value={data.today}
            icon={Activity}
            color="text-yellow-400"
          />

          <StatCard
            title="Top Threat"
            value={data.top_attack ?? "-"}
            icon={Globe}
            color="text-green-400"
          />

        </div>

      </section>

      {/* ===================== INFRASTRUCTURE HEALTH ===================== */}

      <section className="space-y-5">

        <SectionHeader
          title="Infrastructure Health"
          subtitle="Operational status of core platform services"
        />

        <SystemHealthCard />

      </section>

      {/* ===================== THREAT INTELLIGENCE ===================== */}

      <section className="space-y-5">

        <SectionHeader
          title="Threat Intelligence"
          subtitle="Real-time attack trends and severity distribution"
        />

        <div className="grid gap-6 xl:grid-cols-2">

          <ChartCard
            title="Threat Trend"
            subtitle="Network activity during the last 24 hours"
          >
            <ThreatTrendChart />
          </ChartCard>

          <ChartCard
            title="Severity Distribution"
            subtitle="Current alert severity breakdown"
          >
            <SeverityChart />
          </ChartCard>

        </div>

      </section>

      {/* ===================== LIVE THREAT FEED ===================== */}

      <section className="space-y-5">

        <SectionHeader
          title="Live Threat Feed"
          subtitle="Real-time security events detected across the network"
        />

        <RecentEventsTable />

      </section>

    </div>
  );
}