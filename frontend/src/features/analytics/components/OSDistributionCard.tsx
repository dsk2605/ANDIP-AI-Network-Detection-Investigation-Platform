import Card from "@/components/ui/Card";

import type { OSDistribution } from "../types/analytics";

interface Props {
  data: OSDistribution[];
}

export default function OSDistributionCard({
  data,
}: Props) {

  const max =
    Math.max(...data.map((item) => item.count), 1);

  return (
    <Card className="p-6">

      <h2 className="mb-6 text-lg font-semibold text-white">
        Operating System Distribution
      </h2>

      <div className="space-y-5">

        {data.map((item) => (
          <div key={item.operating_system}>

            <div className="mb-2 flex items-center justify-between">

              <span className="text-sm text-slate-300">
                {item.operating_system}
              </span>

              <span className="text-sm font-semibold text-cyan-400">
                {item.count}
              </span>

            </div>

            <div className="h-2 overflow-hidden rounded-full bg-slate-800">

              <div
                className="h-full rounded-full bg-cyan-500 transition-all duration-500"
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