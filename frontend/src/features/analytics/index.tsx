import PageHeader from "@/components/shared/PageHeader";

import AnalyticsStats from "./components/AnalyticsStats";
import TopRiskAssetsTable from "./components/TopRiskAssetsTable";
import OSDistributionCard from "./components/OSDistributionCard";
import EnvironmentDistributionCard from "./components/EnvironmentDistributionCard";
import AssetTypeDistributionCard from "./components/AssetTypeDistributionCard";
import DiscoverySummaryCard from "./components/DiscoverySummaryCard";
import RecommendationPanel from "./components/RecommendationPanel";
import SeverityChart from "./components/SeverityChart";
import ThreatTrendChart from "./components/ThreatTrendChart";

import {
  useAnalytics,
  useSeverityDistribution,
  useThreatTrend,
  useTopRiskAssets,
  useOSDistribution,
  useEnvironmentDistribution,
  useAssetTypeDistribution,
  useSecurityRecommendations,
  useDiscoverySummary,
} from "./hooks/useAnalytics";

export default function AnalyticsPage() {
  const {
    data: analytics,
    isLoading,
    error,
  } = useAnalytics();

  const {
    data: topRiskAssets,
    isLoading: topRiskLoading,
    error: topRiskError,
  } = useTopRiskAssets();

  const {
    data: osDistribution,
  } = useOSDistribution();

  const {
    data: environmentDistribution,
  } = useEnvironmentDistribution();

  const {
    data: assetTypeDistribution,
  } = useAssetTypeDistribution();

  const {
    data: discoverySummary,
  } = useDiscoverySummary();

  const {
    data: recommendations,
  } = useSecurityRecommendations();

  const {
    data: severityData,
    isLoading: severityLoading,
  } = useSeverityDistribution();

  const {
    data: trendData,
    isLoading: trendLoading,
  } = useThreatTrend();

  if (isLoading) {
    return (
      <div className="text-slate-400">
        Loading analytics...
      </div>
    );
  }

  if (error || !analytics) {
    return (
      <div className="text-red-500">
        Failed to load analytics.
      </div>
    );
  }

  return (
    <div className="space-y-8">

      <PageHeader
        title="Security Analytics"
        subtitle="Organization-wide security insights"
      />

      <AnalyticsStats
        analytics={analytics}
      />

      <TopRiskAssetsTable
        assets={topRiskAssets ?? []}
        isLoading={topRiskLoading}
        error={topRiskError}
      />

      <div className="grid gap-6 xl:grid-cols-2">

        {osDistribution && (
          <OSDistributionCard
            data={osDistribution}
          />
        )}

        {environmentDistribution && (
          <EnvironmentDistributionCard
            data={environmentDistribution}
          />
        )}

      </div>

      <div className="grid gap-6 xl:grid-cols-2">

        {assetTypeDistribution && (
          <AssetTypeDistributionCard
            data={assetTypeDistribution}
          />
        )}

        {discoverySummary && (
          <DiscoverySummaryCard
            summary={discoverySummary}
          />
        )}

      </div>

      {recommendations && (
        <RecommendationPanel
          recommendations={recommendations}
        />
      )}

      <div className="grid gap-6 xl:grid-cols-2">

        {!trendLoading &&
          trendData && (
            <ThreatTrendChart
              data={trendData}
            />
          )}

        {!severityLoading &&
          severityData && (
            <SeverityChart
              data={severityData}
            />
          )}

      </div>

    </div>
  );
}