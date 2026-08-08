import Badge from "@/components/ui/Badge";

interface Props {
  status: string;
}

export default function DiscoveryStatusBadge({
  status,
}: Props) {
  switch (status) {
    case "COMPLETED":
      return (
        <Badge variant="success">
          Completed
        </Badge>
      );

    case "RUNNING":
      return (
        <Badge variant="medium">
          Running
        </Badge>
      );

    case "FAILED":
      return (
        <Badge variant="critical">
          Failed
        </Badge>
      );

    default:
      return (
        <Badge variant="low">
          Pending
        </Badge>
      );
  }
}