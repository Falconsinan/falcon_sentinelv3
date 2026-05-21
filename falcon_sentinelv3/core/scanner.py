import re
from collections import Counter, defaultdict

ip_pattern = re.compile(
r"\b(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(?:\.(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}\b"
)

def scan_log(file):

    failed = 0
    success = 0

    ip_counter = Counter()
    failed_ip = defaultdict(int)

    with open(file, "r", errors="ignore") as f:

        for line in f:

            match = ip_pattern.search(line)
            if not match:
                continue

            ip = match.group()
            ip_counter[ip] += 1

            lower = line.lower()

            if "failed password" in lower:
                failed += 1
                failed_ip[ip] += 1

            elif "accepted password" in lower:
                success += 1

    return failed, success, ip_counter, failed_ip