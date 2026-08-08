import Card from "@/components/ui/Card";

import type { AssetTypeDistribution } from "../types/analytics";

interface Props {
  data: AssetTypeDistribution[];
}

export default function AssetTypeDistributionCard({
  data,
}: Props) {

  const max =
    Math.max(...data.map(item => item.count), 1);

  return (
    <Card className="p-6">

      <h2 className="mb-6 text-lg font-semibold text-white">
        Asset Type Distribution
      </h2>

      <div className="space-y-5">

        {data.map((item) => (

          <div key={item.asset_type}>

            <div className="mb-2 flex justify-between">

              <span className="text-sm text-slate-300">
                {item.asset_type}
              </span>

              <span className="font-semibold text-purple-400">
                {item.count}
              </span>

            </div>

            <div className="h-2 rounded-full bg-slate-800">

              <div
                className="h-full rounded-full bg-purple-500"
                style={{
                  width: `${item.count / max * 100}%`,
                }}
              />

            </div>

          </div>

        ))}

      </div>

    </Card>
  );
}