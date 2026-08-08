interface Props {
  label: string;
  status: "online" | "warning" | "offline";
}

const colors = {
  online: "bg-green-500",
  warning: "bg-yellow-500",
  offline: "bg-red-500",
};

export default function StatusIndicator({
  label,
  status,
}: Props) {
  return (
    <div className="flex items-center justify-between rounded-lg border border-slate-800 bg-slate-900 px-4 py-3">
      <span className="text-sm text-slate-300">
        {label}
      </span>

      <span
        className={`h-2.5 w-2.5 rounded-full ${colors[status]}`}
      />
    </div>
  );
}