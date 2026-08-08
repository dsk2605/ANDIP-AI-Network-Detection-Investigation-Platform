import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

import Card from "@/components/ui/Card";

import type { ThreatTrend } from "../types/analytics";

interface Props {
  data: ThreatTrend[];
}

export default function ThreatTrendChart({
  data,
}: Props) {
  return (
    <Card className="p-6">

      <h3 className="mb-6 text-lg font-semibold text-white">
        Threat Trend
      </h3>

      <div className="h-80">

        <ResponsiveContainer width="100%" height="100%">

          <LineChart data={data}>

            <CartesianGrid
              stroke="#334155"
              strokeDasharray="3 3"
            />

            <XAxis
              dataKey="time"
              stroke="#94a3b8"
            />

            <YAxis
              stroke="#94a3b8"
            />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="alerts"
              stroke="#06b6d4"
              strokeWidth={3}
              dot={{ r: 4 }}
              activeDot={{ r: 6 }}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </Card>
  );
}