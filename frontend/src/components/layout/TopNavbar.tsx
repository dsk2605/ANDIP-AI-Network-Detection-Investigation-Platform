import { Bell, UserCircle } from "lucide-react";

export default function TopNavbar() {
  return (
    <header className="h-16 border-b border-slate-800 bg-slate-900 flex items-center justify-between px-6">

      <div>
        <h2 className="text-lg font-semibold text-white">
          Security Operations Center
        </h2>

        <p className="text-xs text-slate-400">
          Monitor · Detect · Respond
        </p>
      </div>

      <div className="flex items-center gap-5 text-slate-300">
        <Bell className="cursor-pointer" />
        <UserCircle size={30} className="cursor-pointer" />
      </div>

    </header>
  );
}