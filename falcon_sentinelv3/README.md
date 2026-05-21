# FALCON Sentinel V3

Advanced AI-Powered Security Monitoring & Intrusion Detection Tool

---

## Overview

FALCON Sentinel V3 is a Python-based cybersecurity monitoring tool designed to detect suspicious activities from log files, identify anomalies, alert administrators, and optionally block malicious IP addresses automatically.

It combines:
- Log scanning
- AI-based anomaly detection
- Telegram alerts
- Auto IP blocking
- Attack visualization

---

## Features

- Real-time log scanning
- AI anomaly detection
- Automatic malicious IP blocking
- Telegram alert integration
- Attack summary reports
- Attack map generation
- Modular architecture
- Easy configuration

---

## Project Structure

```bash
FALCON/
│
├── falcon.py
├── config.json
│
├── core/
│   ├── scanner.py
│   ├── ai_detection.py
│   └── blocker.py
│
├── alerts/
│   └── telegram_alert.py
│
├── visual/
│   └── attack_map.py
│
├── logs/
│   └── access.log
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
cd FALCON
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install requests folium
```

---

## Configuration

Edit `config.json`

Example:

```json
{
    "log_file": "logs/access.log",
    "telegram_alerts": true,
    "auto_block": false
}
```

---

## Run FALCON

```bash
python falcon.py
```

Or:

```bash
python3 falcon.py
```

---

## Telegram Alerts Setup

Inside:

```bash
alerts/telegram_alert.py
```

Add:
- Telegram Bot Token
- Chat ID

Example:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

## Auto Blocking

Enable in config:

```json
"auto_block": true
```

FALCON will automatically attempt to block suspicious IP addresses.

> Root/sudo permissions may be required.

---

## Attack Map

FALCON can generate attack visualization maps for detected attacks.

Generated maps help visualize:
- Attacker locations
- Attack frequency
- Threat regions

---

## Example Output

```bash
[+] Starting Falcon Sentinel V3...
[+] Scanning log file: logs/access.log

========== ATTACK SUMMARY ==========
192.168.1.10  -->  5 attacks
10.0.0.5      -->  2 attacks
====================================

[+] Attack map generated.
```

---

## Requirements

- Python 3.8+
- Linux recommended
- Internet connection for Telegram alerts

---

## Disclaimer

This tool is created for:
- Educational purposes
- Security monitoring
- Defensive cybersecurity research

Do NOT use this project for illegal activities.

---

## Author

SINAN

FALCON Security Project

---

## License

MIT License

Free to use, modify, and distribute.