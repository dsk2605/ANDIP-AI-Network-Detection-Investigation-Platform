import clsx from "clsx";
import { AlertTriangle, ShieldAlert, CheckCircle2, Info } from "lucide-react";

interface Props {
  children: React.ReactNode;
  variant?: "critical" | "high" | "medium" | "low" | "success";
}

const styles = {
  critical: {
    className:
      "border border-red-500/30 bg-red-500/10 text-red-400",
    icon: AlertTriangle,
  },
  high: {
    className:
      "border border-orange-500/30 bg-orange-500/10 text-orange-400",
    icon: ShieldAlert,
  },
  medium: {
    className:
      "border border-yellow-500/30 bg-yellow-500/10 text-yellow-400",
    icon: AlertTriangle,
  },
  low: {
    className:
      "border border-blue-500/30 bg-blue-500/10 text-blue-400",
    icon: Info,
  },
  success: {
    className:
      "border border-emerald-500/30 bg-emerald-500/10 text-emerald-400",
    icon: CheckCircle2,
  },
};

export default function Badge({
  children,
  variant = "low",
}: Props) {
  const config = styles[variant];
  const Icon = config.icon;

  return (
    <span
      className={clsx(
        `
        inline-flex
        items-center
        gap-1.5

        rounded-full

        px-3
        py-1.5

        text-[11px]
        font-semibold
        uppercase
        tracking-[0.12em]

        backdrop-blur-sm
        `,
        config.className
      )}
    >
      <Icon size={12} strokeWidth={2.3} />
      {children}
    </span>
  );
}