#!/usr/bin/env python3

import json
import time
from collections import Counter

# =========================
# Import Modules
# =========================
try:
    from core.scanner import scan_logs
    from core.ai_detection import detect_anomalies
    from core.blocker import block_ip
    from alerts.telegram_alert import send_telegram_alert
    from visual.attack_map import generate_attack_map

except Exception as e:
    print(f"[ERROR] Import failed: {e}")
    exit(1)

# =========================
# Config Loader
# =========================
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)

    except Exception as e:
        print(f"[ERROR] Cannot load config: {e}")
        return {}

# =========================
# Print Attack Summary
# =========================
def print_summary(results):
    print("\n========== ATTACK SUMMARY ==========")

    ip_counter = Counter()

    for item in results:
        ip = item.get("ip", "unknown")
        ip_counter[ip] += 1

    for ip, count in ip_counter.items():
        print(f"{ip}  -->  {count} attacks")

    print("====================================\n")

# =========================
# Safe IP Blocking
# =========================
def safe_block_ip(ip):
    try:
        print(f"[+] Blocking IP: {ip}")
        block_ip(ip)

    except Exception as e:
        print(f"[ERROR] Failed to block {ip}: {e}")

# =========================
# Handle Alerts
# =========================
def handle_alerts(results, config):
    telegram_enabled = config.get("telegram_alerts", False)

    for item in results:
        ip = item.get("ip", "unknown")
        attack = item.get("attack", "Unknown Attack")

        message = f"""
🚨 FALCON ALERT 🚨

IP: {ip}
Attack: {attack}
Time: {time.ctime()}
"""

        print(message)

        if telegram_enabled:
            try:
                send_telegram_alert(message)

            except Exception as e:
                print(f"[ERROR] Telegram alert failed: {e}")

# =========================
# Main Scan Function
# =========================
def run_scan():
    config = load_config()

    log_file = config.get("log_file", "logs/access.log")

    print("[+] Starting Falcon Sentinel V3...")
    print(f"[+] Scanning log file: {log_file}")

    # Scan Logs
    results = scan_logs(log_file)

    if not results:
        print("[+] No suspicious activity detected.")
        return

    # AI Detection
    suspicious = detect_anomalies(results)

    # Print Summary
    print_summary(suspicious)

    # Alerts
    handle_alerts(suspicious, config)

    # Auto Block
    if config.get("auto_block", False):
        for item in suspicious:
            ip = item.get("ip")

            if ip:
                safe_block_ip(ip)

    # Generate Attack Map
    try:
        generate_attack_map(suspicious)
        print("[+] Attack map generated.")

    except Exception as e:
        print(f"[ERROR] Failed to generate map: {e}")

# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    run_scan()