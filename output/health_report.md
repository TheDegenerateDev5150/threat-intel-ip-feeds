# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T14:26:50.299781+00:00
**Duration:** 42.9s
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
| Unique to single source | 59,965 |
| Found in multiple sources | 45,471 |
| Max source overlap | 9 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 32,257 | 25,474 | 55.9% |
| SGB (Turkiye) | 9,777 | 223 | 97.8% |
| Stamparm IPsum | 7,249 | 31,474 | 18.7% |
| CINS Army | 5,809 | 9,191 | 38.7% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,128 | 3,636 | 23.7% |
| AbuseIPDB | 763 | 9,237 | 7.6% |
| Tor Exit Nodes | 619 | 645 | 49.0% |
| GreenSnow | 351 | 4,915 | 6.7% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 42 | 21,516 | 0.2% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 330 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,655 | 0.0% |
| Blocklist.de (mail) | 0 | 12,750 | 0.0% |
| Blocklist.de (apache) | 0 | 8,980 | 0.0% |
| Blocklist.de (bots) | 0 | 1,670 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 825 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,397 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,750 |
| Blocklist.de (all) & Stamparm IPsum | 9,744 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,980 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,474 |
| Stamparm IPsum & AbuseIPDB | 8,419 |
| CINS Army & Stamparm IPsum | 8,204 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,166 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,655 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 72 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,731 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 21,558 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,750 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,980 | OK |
| Blocklist.de (ssh) | 5,655 | OK |
| GreenSnow | 5,266 | OK |
| BinaryDefense | 4,764 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,670 | OK |
| Tor Exit Nodes | 1,264 | OK |
| Blocklist.de (bruteforcelogin) | 825 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
