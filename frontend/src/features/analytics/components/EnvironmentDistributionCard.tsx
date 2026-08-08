import Card from "@/components/ui/Card";

import type { EnvironmentDistribution } from "../types/analytics";

interface Props {
  data: EnvironmentDistribution[];
}

export default function EnvironmentDistributionCard({
  data,
}: Props) {

  const max =
    Math.max(...data.map((item) => item.count), 1);

  return (
    <Card className="p-6">

      <h2 className="mb-6 text-lg font-semibold text-white">
        Environment Distribution
      </h2>

      <div className="space-y-5">

        {data.map((item) => (
          <div key={item.environment}>

            <div className="mb-2 flex items-center justify-between">

              <span className="text-sm text-slate-300">
                {item.environment}
              </span>

              <span className="text-sm font-semibold text-green-400">
                {item.count}
              </span>

            </div>

            <div className="h-2 overflow-hidden rounded-full bg-slate-800">

              <div
                className="h-full rounded-full bg-green-500 transition-all duration-500"
                style={{
                  width: `${(item.count / max) * 100}%`,
                }}
              />

            </div>

          </div>
        ))}

      </div>

    </Card>
  );
}