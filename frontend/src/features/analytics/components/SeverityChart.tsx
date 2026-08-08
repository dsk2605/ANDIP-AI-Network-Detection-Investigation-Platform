import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import Card from "@/components/ui/Card";

import type { SeverityDistribution } from "../types/analytics";

interface Props {
  data: SeverityDistribution[];
}

const COLORS = [
  "#ef4444",
  "#f97316",
  "#eab308",
  "#22c55e",
];

export default function SeverityChart({
  data,
}: Props) {
  return (
    <Card className="p-6">
      <h3 className="mb-6 text-lg font-semibold text-white">
        Alert Severity Distribution
      </h3>

      <div className="h-80">
        <ResponsiveContainer>
          <PieChart>
            <Pie
              data={data}
              dataKey="count"
              nameKey="severity"
              outerRadius={110}
            >
              {data.map((_, index) => (
                <Cell
                  key={index}
                  fill={
                    COLORS[
                      index % COLORS.length
                    ]
                  }
                />
              ))}
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </Card>
  );
}