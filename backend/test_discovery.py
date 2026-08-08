from app.discovery.discovery_service import DiscoveryService

service = DiscoveryService()

results = service.discover("scanme.nmap.org")

print(results)