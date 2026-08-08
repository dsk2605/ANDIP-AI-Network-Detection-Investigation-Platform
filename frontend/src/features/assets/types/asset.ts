export interface Asset {
  id: string;

  hostname: string;

  ip_address: string;

  mac_address: string;

  operating_system: string;

  asset_type:
    | "SERVER"
    | "WORKSTATION"
    | "NETWORK_DEVICE"
    | "OTHER";

  environment:
    | "PRODUCTION"
    | "STAGING"
    | "DEVELOPMENT"
    | "LAB";

  status:
    | "ACTIVE"
    | "INACTIVE"
    | "UNKNOWN";

  last_seen: string | null;

  risk_score: number;

  is_monitored: boolean;
}