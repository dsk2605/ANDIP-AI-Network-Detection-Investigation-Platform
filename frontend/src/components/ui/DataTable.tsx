import type { ReactNode } from "react";

import Card from "./Card";

interface DataTableProps {
  title?: string;
  columns: ReactNode;
  children: ReactNode;
  footer?: ReactNode;
  isLoading?: boolean;
  error?: unknown;
  emptyMessage?: string;
}

export default function DataTable({
  title,
  columns,
  children,
  footer,
  isLoading = false,
  error,
  emptyMessage = "No data available.",
}: DataTableProps) {
  return (
    <Card className="overflow-hidden">

      {title && (
        <div className="border-b border-slate-800 px-6 py-5">
          <h2 className="text-lg font-semibold text-white">
            {title}
          </h2>
        </div>
      )}

      {isLoading ? (
        <div className="p-8 text-center text-slate-400">
          Loading...
        </div>
      ) : error ? (
        <div className="p-8 text-center text-red-400">
          Failed to load data.
        </div>
      ) : (
        <div className="overflow-x-auto">

          <table className="min-w-full">

            <thead className="border-b border-slate-800 bg-slate-950">
              {columns}
            </thead>

            <tbody className="divide-y divide-slate-800">

              {children || (
                <tr>
                  <td
                    colSpan={100}
                    className="px-6 py-8 text-center text-slate-400"
                  >
                    {emptyMessage}
                  </td>
                </tr>
              )}

            </tbody>

          </table>

        </div>
      )}

      {footer && (
        <div className="border-t border-slate-800 bg-slate-950/40 px-6 py-4">
          {footer}
        </div>
      )}

    </Card>
  );
}