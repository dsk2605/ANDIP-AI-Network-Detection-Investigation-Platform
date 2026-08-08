import Badge from "@/components/ui/Badge";

interface Props {
  severity: string;
}

export default function SeverityBadge({
  severity,
}: Props) {
  const value = severity.toLowerCase();

  const variant =
    value === "critical"
      ? "critical"
      : value === "high"
      ? "high"
      : value === "medium"
      ? "medium"
      : "low";

  return (
    <Badge variant={variant}>
      {severity}
    </Badge>
  );
}