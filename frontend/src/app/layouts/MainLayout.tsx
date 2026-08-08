import AppRouter from "../router";
import Sidebar from "@/components/layout/Sidebar";
import TopNavbar from "@/components/layout/TopNavbar";
import PageContainer from "@/components/layout/PageContainer";

export default function MainLayout() {
  return (
    <div className="flex h-screen bg-slate-900">

      <Sidebar />

      <div className="flex flex-1 flex-col">

        <TopNavbar />

        <PageContainer>
          <AppRouter />
        </PageContainer>

      </div>

    </div>
  );
}