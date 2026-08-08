import { Activity } from "lucide-react";

interface Props {
  lastUpdated: Date;
}

export default function LiveStatus({
  lastUpdated,
}: Props) {
  return (
    <div className="flex items-center justify-between rounded-xl border border-green-900/30 bg-green-950/10 px-5 py-4">

      <div className="flex items-center gap-3">

        <Activity
          size={18}
          className="animate-pulse text-green-400"
        />

        <div>

          <p className="font-medium text-green-400">
            LIVE Monitoring
          </p>

          <p className="text-xs text-slate-400">
            Auto refresh every 5 seconds
          </p>

        </div>

      </div>

      <div className="text-right">

        <p className="text-xs text-slate-500">
          Last Updated
        </p>

        <p className="font-mono text-sm text-white">
          {lastUpdated.toLocaleTimeString()}
        </p>

      </div>

    </div>
  );
}