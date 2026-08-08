import type { LucideIcon } from "lucide-react";
import Card from "@/components/ui/Card";

interface Props {
  title: string;
  value: number | string;
  icon: LucideIcon;
  color?: string;
  subtitle?: string;
}

export default function StatCard({
  title,
  value,
  icon: Icon,
  color = "text-cyan-400",
  subtitle = "Live • Updated just now",
}: Props) {
  const isNumber = typeof value === "number";

  const valueClass = isNumber
    ? "text-5xl"
    : String(value).length > 14
    ? "text-3xl"
    : "text-4xl";

  return (
    <Card
      className="
        group
        relative
        overflow-hidden
        border
        border-slate-800
        bg-gradient-to-br
        from-slate-900
        via-slate-900
        to-slate-950
        transition-all
        duration-300
        hover:-translate-y-1
        hover:border-cyan-500/40
        hover:shadow-xl
        hover:shadow-cyan-500/10
      "
    >
      {/* Top Accent */}
      <div className="absolute left-0 top-0 h-1 w-full bg-gradient-to-r from-cyan-500 via-blue-500 to-indigo-500" />

      <div className="flex items-start justify-between p-6">

        {/* Left */}

        <div className="flex-1">

          <p className="mt-2 text-[11px] font-bold uppercase tracking-[0.30em] text-slate-500">
            {title}
          </p>

          <h2
            className={`
              mt-5
              font-bold
              leading-tight
              tracking-tight
              text-white
              break-words
              ${valueClass}
            `}
          >
            {value}
          </h2>

          <div className="mt-6 flex items-center gap-2">

            <div className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse" />

            <span className="text-xs text-slate-400">
              {subtitle}
            </span>

          </div>

        </div>

        {/* Icon */}

        <div
          className={`
            ml-5
            flex
            h-14
            w-14
            shrink-0
            items-center
            justify-center
            rounded-xl
            border
            border-slate-700
            bg-slate-800/70
            backdrop-blur-sm
            transition-all
            duration-300
            group-hover:scale-105
            group-hover:border-cyan-500/40
            ${color}
          `}
        >
          <Icon size={24} strokeWidth={2.2} />
        </div>

      </div>

    </Card>
  );
}