import type { ReactNode } from "react";

interface Props {
    children: ReactNode;
}

export default function PageContainer({
    children,
}: Props) {

    return (
        <main className="flex-1 overflow-auto p-8">
            {children}
        </main>
    );
}