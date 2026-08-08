import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import { useThreatTrend } from "@/hooks/useDashboard";

export default function ThreatTrendChart() {
  const { data, isLoading, error } = useThreatTrend();

  if (isLoading) {
    return (
      <div className="flex h-full items-center justify-center text-slate-400">
        Loading threat trend...
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex h-full items-center justify-center text-red-400">
        Failed to load threat trend.
      </div>
    );
  }

  if (!data || data.length === 0) {
    return (
      <div className="flex h-full items-center justify-center text-slate-500">
        No threat data available.
      </div>
    );
  }

  return (
    <ResponsiveContainer width="100%" height={390}>
      <AreaChart
        data={data}
        margin={{
          top: 10,
          right: 30,
          left: 15,
          bottom: 10,
        }}
      >
        <defs>
          <linearGradient
            id="threatGradient"
            x1="0"
            y1="0"
            x2="0"
            y2="1"
          >
            <stop
              offset="5%"
              stopColor="#3B82F6"
              stopOpacity={0.45}
            />

            <stop
              offset="95%"
              stopColor="#3B82F6"
              stopOpacity={0}
            />
          </linearGradient>
        </defs>

        <CartesianGrid
          stroke="#1E293B"
          strokeDasharray="4 4"
          vertical={false}
        />

        <XAxis
          dataKey="time"
          tick={{
            fill: "#94A3B8",
            fontSize: 11,
          }}
          tickMargin={10}
          minTickGap={28}
          interval="preserveStartEnd"
          tickLine={false}
          axisLine={false}
          padding={{
            left: 10,
            right: 10,
          }}
        />

        <YAxis
          tick={{
            fill: "#94A3B8",
            fontSize: 11,
          }}
          tickMargin={10}
          tickLine={false}
          axisLine={false}
          allowDecimals={false}
          width={45}
        />

        <Tooltip
          cursor={{
            stroke: "#3B82F6",
            strokeDasharray: "5 5",
          }}
          contentStyle={{
            background: "#0F172A",
            border: "1px solid #334155",
            borderRadius: 12,
          }}
          labelStyle={{
            color: "#fff",
          }}
        />

        <Area
          type="monotone"
          dataKey="alerts"
          stroke="#3B82F6"
          strokeWidth={3}
          fill="url(#threatGradient)"
          dot={false}
          activeDot={{
            r: 6,
            fill: "#3B82F6",
            stroke: "#FFFFFF",
            strokeWidth: 2,
          }}
        />

      </AreaChart>
    </ResponsiveContainer>
  );
}