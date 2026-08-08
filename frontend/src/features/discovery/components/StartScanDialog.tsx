import { useState } from "react";

interface Props {
  open: boolean;
  loading: boolean;
  onClose: () => void;
  onStart: (target: string) => void;
}

export default function StartScanDialog({
  open,
  loading,
  onClose,
  onStart,
}: Props) {
  const [target, setTarget] = useState("");

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">

      <div className="w-full max-w-md rounded-xl border border-slate-800 bg-slate-900 p-6">

        <h2 className="mb-2 text-xl font-semibold text-white">
          Start Discovery Scan
        </h2>

        <p className="mb-6 text-sm text-slate-400">
          Enter an IP, subnet or hostname to scan.
        </p>

        <input
          value={target}
          onChange={(e) => setTarget(e.target.value)}
          placeholder="192.168.1.0/24 or scanme.nmap.org"
          className="mb-3 w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3 text-white outline-none focus:border-cyan-500"
        />

        <p className="mb-6 text-xs text-slate-500">
          Examples:
          <br />
          • 192.168.1.0/24
          <br />
          • scanme.nmap.org
        </p>

        <div className="flex justify-end gap-3">

          <button
            onClick={onClose}
            className="rounded-lg border border-slate-700 px-4 py-2 text-slate-300 hover:text-white"
          >
            Cancel
          </button>

          <button
            disabled={!target || loading}
            onClick={() => onStart(target)}
            className="rounded-lg bg-cyan-600 px-4 py-2 text-white transition hover:bg-cyan-500 disabled:opacity-50"
          >
            {loading ? "Scanning..." : "Start Scan"}
          </button>

        </div>

      </div>

    </div>
  );
}