# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T20:40:56.252554+00:00
**Duration:** 38.54s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| SGB (Turkiye) | HttpError: HTTP 429: <html>
<head><title>429 Too Many Requests</title></head>
<body>
<center><h1>429 Too Many Requests</h1></center>
<hr><center>nginx</center>
</body>
</html>
 | 10,000 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 61,643 |
| Found in multiple sources | 45,583 |
| Max source overlap | 9 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 33,385 | 27,674 | 54.7% |
| SGB (Turkiye) | 9,767 | 233 | 97.7% |
| Stamparm IPsum | 7,274 | 31,449 | 18.8% |
| CINS Army | 6,187 | 8,813 | 41.2% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,117 | 3,647 | 23.4% |
| AbuseIPDB | 990 | 9,010 | 9.9% |
| Tor Exit Nodes | 615 | 646 | 48.8% |
| GreenSnow | 316 | 5,156 | 5.8% |
| AlienVault OTX | 146 | 22 | 86.9% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 31 | 21,347 | 0.1% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 331 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,650 | 0.0% |
| Blocklist.de (mail) | 0 | 12,765 | 0.0% |
| Blocklist.de (apache) | 0 | 8,942 | 0.0% |
| Blocklist.de (bots) | 0 | 1,511 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 779 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,823 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,765 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,011 |
| Blocklist.de (all) & Stamparm IPsum | 9,601 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,942 |
| Stamparm IPsum & AbuseIPDB | 8,060 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,803 |
| RTBH (Turkiye) & AbuseIPDB | 6,960 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,650 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 75 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 61,059 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 21,378 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,765 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,942 | OK |
| Blocklist.de (ssh) | 5,650 | OK |
| GreenSnow | 5,472 | OK |
| BinaryDefense | 4,764 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,511 | OK |
| Tor Exit Nodes | 1,261 | OK |
| Blocklist.de (bruteforcelogin) | 779 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 338 | OK |
| AlienVault OTX | 168 | OK |
| Spamhaus DROPv6 | 94 | OK |
