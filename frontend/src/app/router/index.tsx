import { Routes, Route, Navigate } from "react-router-dom";

import DashboardPage from "@/features/dashboard";
import AlertsPage from "@/features/alerts";
import AssetsPage from "@/features/assets";
import DiscoveryPage from "@/features/discovery";
import AnalyticsPage from "@/features/analytics";
import SettingsPage from "@/features/settings";

export default function AppRouter() {
    return (
        <Routes>

            <Route
                path="/"
                element={<Navigate to="/dashboard" replace />}
            />

            <Route
                path="/dashboard"
                element={<DashboardPage />}
            />

            <Route
                path="/alerts"
                element={<AlertsPage />}
            />

            <Route
                path="/assets"
                element={<AssetsPage />}
            />

            <Route
                path="/discovery"
                element={<DiscoveryPage />}
            />

            <Route
                path="/analytics"
                element={<AnalyticsPage />}
            />

            <Route
                path="/settings"
                element={<SettingsPage />}
            />

        </Routes>
    );
}