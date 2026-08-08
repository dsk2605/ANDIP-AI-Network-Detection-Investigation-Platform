import type { ReactNode } from "react";

interface Props {
  children: ReactNode;
}

export default function PageToolbar({
  children,
}: Props) {
  return (
    <div className="mb-6 flex flex-wrap items-center justify-between gap-4 rounded-xl border border-slate-800 bg-slate-900 p-4">
      {children}
    </div>
  );
}