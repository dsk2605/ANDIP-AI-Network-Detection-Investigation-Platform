import {
  BarChart3,
  LayoutDashboard,
  Monitor,
  Search,
  Settings,
  Shield,
  ShieldAlert,
} from "lucide-react";
import { NavLink } from "react-router-dom";

const menu = [
  {
    name: "Dashboard",
    path: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "Alerts",
    path: "/alerts",
    icon: ShieldAlert,
  },
  {
    name: "Assets",
    path: "/assets",
    icon: Monitor,
  },
  {
    name: "Discovery",
    path: "/discovery",
    icon: Search,
  },
  {
    name: "Analytics",
    path: "/analytics",
    icon: BarChart3,
  },
  {
    name: "Settings",
    path: "/settings",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="flex w-72 flex-col border-r border-slate-800 bg-slate-950">

      {/* Logo */}

      <div className="border-b border-slate-800 px-7 py-7">

        <div className="flex items-center gap-3">

          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-cyan-500/10 text-cyan-400">

            <Shield size={24} />

          </div>

          <div>

            <h1 className="text-xl font-bold tracking-wide text-white">
              ANDIP
            </h1>

            <p className="text-xs text-slate-500">
              Network Detection Platform
            </p>

          </div>

        </div>

      </div>

      {/* Navigation */}

      <nav className="flex-1 px-4 py-6">

        <p className="mb-4 px-3 text-xs font-semibold uppercase tracking-[0.18em] text-slate-600">
          Navigation
        </p>

        <div className="space-y-2">

          {menu.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  `
                  group
                  flex
                  items-center
                  gap-3
                  rounded-xl
                  px-4
                  py-3
                  transition-all
                  duration-200

                  ${
                    isActive
                      ? "border border-cyan-500/20 bg-cyan-500/10 text-cyan-400"
                      : "text-slate-400 hover:bg-slate-900 hover:text-white"
                  }
                `
                }
              >
                <Icon
                  size={19}
                  className="transition-transform duration-200 group-hover:scale-110"
                />

                <span className="text-sm font-medium">
                  {item.name}
                </span>

              </NavLink>
            );
          })}

        </div>

      </nav>

      {/* Footer */}

      <div className="border-t border-slate-800 px-6 py-5">

        <div className="flex items-center justify-between">

          <div>

            <p className="text-sm font-medium text-slate-300">
              ANDIP
            </p>

            <p className="text-xs text-slate-500">
              Version 1.0.0
            </p>

          </div>

          <div className="flex items-center gap-2">

            <div className="h-2.5 w-2.5 rounded-full bg-emerald-400" />

            <span className="text-xs text-emerald-400">
              Online
            </span>

          </div>

        </div>

      </div>

    </aside>
  );
}