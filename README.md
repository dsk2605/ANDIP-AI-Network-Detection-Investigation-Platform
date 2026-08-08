<div align="center">

# 🛡 ANDIP

## AI Network Detection & Investigation Platform

### Real-Time Network Detection, Analysis & Investigation Platform

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688.svg)]()
[![React](https://img.shields.io/badge/React-19-61DAFB.svg)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

**Detect • Analyze • Investigate**

</div>

---

# 📖 Overview

ANDIP (AI Network Detection & Investigation Platform) is a real-time Network Detection and Investigation Platform (NDIP) designed to monitor live network traffic, analyze network flows, detect cyber threats, and provide actionable insights through an interactive dashboard.

The platform combines packet capture, flow analysis, modular attack detection, and live visualization to help security analysts identify suspicious network activities efficiently. Built with scalability in mind, ANDIP provides a strong foundation for future AI-powered threat detection, investigation, and security analytics.

---

# ✨ Features

- 📡 Real-time Packet Capture
- 🔄 Flow-Based Traffic Analysis
- 🚨 Live Threat Detection
- 📊 Interactive Security Dashboard
- 🌐 Network Asset Discovery
- 📈 Real-Time Analytics
- ⚡ WebSocket-Based Live Updates
- 🐳 Dockerized Infrastructure
- 🗄 PostgreSQL Database
- 🔐 Modular Detection Architecture

---

# 🛡 Supported Attack Detection

|Attack|                |Status|
| Port Scan              | ✅ |
| SYN Flood              | ✅ |
| UDP Flood              | ✅ |
| ICMP Flood             | ✅ |
| DoS                    | ✅ |
| Distributed DoS (DDoS) | ✅ |

---

# 🏗 System Architecture


```
Network Traffic
        │
Packet Capture (Scapy)
        │
Packet Parser
        │
Flow Manager
        │
Detection Engine
        │
├── Port Scan
├── SYN Flood
├── UDP Flood
├── ICMP Flood
├── DoS
└── DDoS
        │
Alert Management
        │
FastAPI + WebSocket
        │
React Dashboard
```

---

# ⚙ Technology Stack

## Backend

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Alembic

## Frontend

- React
- TypeScript
- Tailwind CSS
- Axios
- Recharts

## Networking

- Scapy
- WebSocket
- Flow-Based Analysis
- Sliding Window Detection

## Database

- PostgreSQL
- Redis
- pgAdmin

## DevOps

- Docker
- Docker Compose

## Development & Testing

- VMware Workstation
- Kali Linux
- Windows 11
- Git
- GitHub
- Visual Studio Code
- Nmap
- hping3

---

# 🚀 Getting Started

## Clone Repository



## Start Infrastructure

```bash
docker compose up -d
```

## Backend

```bash
cd backend

uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend

npm install

npm run dev
```


---

# 🚀 Roadmap

## Version 1.0

- [x] Real-Time Packet Capture
- [x] Flow Management
- [x] Detection Engine
- [x] Dashboard
- [x] Port Scan Detection
- [x] SYN Flood Detection
- [x] UDP Flood Detection
- [x] ICMP Flood Detection
- [x] DoS Detection
- [x] DDoS Detection

## Version 2.0

- [ ] AI-Based Anomaly Detection
- [ ] Threat Intelligence Integration
- [ ] MITRE ATT&CK Mapping
- [ ] GeoIP Visualization
- [ ] Email & Slack Notifications
- [ ] PCAP Export
- [ ] Advanced Security Analytics
- [ ] Role-Based Access Control

## Version 3.0

- [ ] SIEM Integration
- [ ] Distributed Network Sensors
- [ ] AI Security Assistant
- [ ] Enterprise Multi-Tenant Support

---

# 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

If you have ideas to improve ANDIP, feel free to fork the repository and submit a pull request.

---

# 👨‍💻 Author

**Dheraya Kamdar**

Cyber Security Engineer

---

# 📜 License

This project is licensed under the MIT License.
