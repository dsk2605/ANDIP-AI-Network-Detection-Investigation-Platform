import Card from "@/components/ui/Card";

import type {
  SecurityRecommendation,
} from "../types/analytics";

interface Props {
  recommendations: SecurityRecommendation[];
}

export default function RecommendationPanel({
  recommendations,
}: Props) {

  return (
    <Card className="p-6">

      <h2 className="mb-6 text-lg font-semibold text-white">
        Security Recommendations
      </h2>

      <div className="space-y-4">

        {recommendations.map((item, index) => {

          const color =
            item.priority === "HIGH"
              ? "border-red-500 bg-red-500/10"
              : item.priority === "MEDIUM"
              ? "border-yellow-500 bg-yellow-500/10"
              : "border-green-500 bg-green-500/10";

          return (

            <div
              key={index}
              className={`rounded-lg border-l-4 p-4 ${color}`}
            >

              <div className="mb-2 flex items-center gap-3">

                <span className="rounded bg-slate-900 px-2 py-1 text-xs font-semibold text-white">

                  {item.priority}

                </span>

              </div>

              <p className="text-slate-300">

                {item.message}

              </p>

            </div>

          );

        })}

      </div>

    </Card>
  );
}