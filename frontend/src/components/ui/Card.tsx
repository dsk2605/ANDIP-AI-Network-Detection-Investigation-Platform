import type { ReactNode } from "react";
import clsx from "clsx";

interface CardProps {
  children: ReactNode;
  className?: string;
}

export default function Card({
  children,
  className,
}: CardProps) {
  return (
    <div
      className={clsx(
        `
        relative
        overflow-hidden

        rounded-2xl

        border
        border-slate-800/80

        bg-gradient-to-br
        from-slate-900
        via-slate-900
        to-slate-950

        shadow-lg
        shadow-black/20

        backdrop-blur-xl

        transition-all
        duration-300
        ease-out

        hover:-translate-y-1
        hover:border-cyan-500/30
        hover:shadow-2xl
        hover:shadow-cyan-500/10
        `,
        className
      )}
    >
      {/* Soft Glow */}
      <div
        className="
          pointer-events-none
          absolute
          inset-0
          bg-gradient-to-br
          from-cyan-500/[0.03]
          via-transparent
          to-transparent
        "
      />

      {children}
    </div>
  );
}