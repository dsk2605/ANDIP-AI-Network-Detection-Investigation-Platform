import Badge from "@/components/ui/Badge";

interface Props {
  status: string;
}

export default function AssetStatusBadge({
  status,
}: Props) {
  switch (status) {
    case "ACTIVE":
      return (
        <Badge variant="success">
          Active
        </Badge>
      );

    case "INACTIVE":
      return (
        <Badge variant="critical">
          Inactive
        </Badge>
      );

    default:
      return (
        <Badge variant="low">
          Unknown
        </Badge>
      );
  }
}