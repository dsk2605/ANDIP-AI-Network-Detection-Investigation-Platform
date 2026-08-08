import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
} from "recharts";

import { useSeverityDistribution } from "@/hooks/useDashboard";

const COLORS = [
  "#EF4444",
  "#F97316",
  "#EAB308",
  "#3B82F6",
];

export default function SeverityChart() {
  const { data, isLoading } = useSeverityDistribution();

  if (isLoading) {
    return (
      <div className="flex h-full items-center justify-center text-slate-400">
        Loading...
      </div>
    );
  }

  if (!data || data.length === 0) {
    return (
      <div className="flex h-full items-center justify-center text-slate-500">
        No alert data available.
      </div>
    );
  }

  return (
    <div className="flex h-full flex-col items-center justify-center gap-5">

      <ResponsiveContainer width="100%" height={260}>
        <PieChart>

          <Pie
            data={data}
            dataKey="count"
            nameKey="severity"
            cx="50%"
            cy="50%"
            innerRadius={65}
            outerRadius={95}
            paddingAngle={3}
          >
            {data.map((_, index) => (
              <Cell
                key={index}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Pie>

          <Tooltip
            contentStyle={{
              background: "#0F172A",
              border: "1px solid #334155",
              borderRadius: 12,
            }}
          />

        </PieChart>
      </ResponsiveContainer>

      {/* Legend */}

      <div className="grid w-full grid-cols-2 gap-3 px-3">

        {data.map((item, index) => (

          <div
            key={item.severity}
            className="flex items-center justify-between rounded-lg border border-slate-800 bg-slate-900/60 px-3 py-2"
          >

            <div className="flex items-center gap-2">

              <div
                className="h-3 w-3 rounded-full"
                style={{
                  backgroundColor:
                    COLORS[index % COLORS.length],
                }}
              />

              <span className="text-sm text-slate-300">
                {item.severity}
              </span>

            </div>

            <span className="font-semibold text-white">
              {item.count}
            </span>

          </div>

        ))}

      </div>

    </div>
  );
}