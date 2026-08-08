import { BarChart3 } from "lucide-react";

export default function ChartPlaceholder() {
  return (
    <div className="flex h-full items-center justify-center rounded-lg border border-dashed border-slate-700 bg-slate-950">
      <div className="text-center">
        <BarChart3
          size={42}
          className="mx-auto text-slate-600"
        />

        <p className="mt-4 text-sm text-slate-500">
          Chart will appear here
        </p>
      </div>
    </div>
  );
}